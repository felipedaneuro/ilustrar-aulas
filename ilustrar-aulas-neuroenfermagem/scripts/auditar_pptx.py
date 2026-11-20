"""Confira a preservação estrutural de um PPTX ilustrado."""
import argparse
from collections import Counter
from hashlib import sha256
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import posixpath

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

def links(package, part):
    folder, filename = posixpath.split(part)
    rels = posixpath.join(folder, '_rels', filename + '.rels')
    if rels not in package.namelist():
        return {}
    return {n.get('Id'): (
        n.get('Type').rsplit('/', 1)[-1],
        posixpath.normpath(posixpath.join(folder, n.get('Target').lstrip('/')))
        if not n.get('Target').startswith('/') else n.get('Target')[1:]
    ) for n in ET.fromstring(package.read(rels)) if n.get('TargetMode') != 'External'}

def text_runs(node):
    return [element.text for element in node.iter(A + 't') if element.text]

def strip_production(tree):
    for parent in tree.iter():
        elements = list(parent)
        for index, element in enumerate(elements):
            content = ''.join(text_runs(element)).strip()
            if element.tag != P+'sp' or not content.startswith('[ IMAGEM '):
                continue
            if index+2 >= len(elements) or not ''.join(text_runs(elements[index+2])).startswith('prompt em PROMPTS_IMAGENS'):
                continue
            for placeholder in elements[index:index+3]:
                parent.remove(placeholder)
            break

def parts(package, ignore_placeholders):
    main = 'ppt/presentation.xml'
    main_tree = ET.fromstring(package.read(main))
    routes = links(package, main)
    results = []
    for pointer in main_tree.findall(f'{P}sldIdLst/{P}sldId'):
        slide = routes[pointer.get(R+'id')][1]
        tree = ET.fromstring(package.read(slide))
        if ignore_placeholders:
            strip_production(tree)
        routes_to_slide = links(package, slide)
        refs = [element.get(R+'embed') for element in tree.iter(A+'blip')]
        photos = Counter(sha256(package.read(routes_to_slide[r][1])).hexdigest() for r in refs if r)
        notes = next((name for mode,name in routes_to_slide.values() if mode=='notesSlide'), None)
        notes_text = text_runs(ET.fromstring(package.read(notes))) if notes else []
        results.append((Counter(text_runs(tree)), photos, Counter(notes_text)))
    return main_tree.find(P+'sldSz').attrib, results

def audit(original, illustrated, require_image):
    errors = []
    with ZipFile(original) as before, ZipFile(illustrated) as after:
        old_size, old = parts(before, True)
        new_size, new = parts(after, False)
    if old_size != new_size:
        errors.append('dimensões da apresentação alteradas')
    if len(old) != len(new):
        errors.append(f'contagem de slides alterada de {len(old)} para {len(new)}')
    for index, ((old_text, old_media, old_notes), (new_text, new_media, new_notes)) in enumerate(zip(old, new), 1):
        for name,missing in (('texto',old_text-new_text),('imagens originais',old_media-new_media),('notas',old_notes-new_notes)):
            if missing:
                errors.append(f'slide {index:02d} perdeu {name} ({sum(missing.values())} ocorrências)')
        if require_image and not (new_media-old_media):
            errors.append(f'slide {index:02d} sem nova imagem incorporada')
    return len(old),errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('original',type=Path)
    parser.add_argument('ilustrado',type=Path)
    parser.add_argument('--exigir-figura-por-slide',action='store_true')
    args=parser.parse_args()
    count,errors=audit(args.original,args.ilustrado,args.exigir_figura_por_slide)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f'{count} slides conferidos — dimensões, texto, imagens e notas preservados.')

if __name__=='__main__':
    main()
