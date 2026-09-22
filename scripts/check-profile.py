#!/usr/bin/env python3
"""Validate the generated, public-facing organization README without network calls."""
from pathlib import Path
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / 'profile'
raw = 'https://raw.githubusercontent.com/aozix-tech/.github/main/profile/assets/'
readme = (PROFILE / 'README.md').read_text(encoding='utf-8')
assert 'Beyond ideas.' in readme and 'Into reality.' in readme
assert 'https://aozix.com/' in readme and 'https://x.com/aozixtech' in readme
assert 'https://github.com/aozhi-tech' not in readme
assert not re.search(r'[\u3400-\u9fff]', readme), 'Public copy must be English'
assert not re.search(r'<(?:script|style|iframe)\b', readme, re.I)
assert len(re.findall(r'<picture>', readme)) == 2
for tag in re.findall(r'<img\b[^>]*>', readme):
    assert re.search(r'alt="[^"]+"', tag), 'Every image needs meaningful alt text'
references = re.findall(r'(?:src|srcset)="([^"]+)"', readme)
expected = {'hero.svg', 'hero-mobile.svg', 'focus.svg', 'focus-mobile.svg'}
assert {url.rsplit('/', 1)[-1] for url in references} == expected
for url in references:
    assert url.startswith(raw), 'Images must come from this public repository'
    name = url.rsplit('/', 1)[-1]
    content = (PROFILE / 'assets' / name).read_text(encoding='utf-8')
    assert len(content.encode()) < 80000, 'Keep each vector asset lightweight'
    root = ET.fromstring(content)
    assert root.tag == '{http://www.w3.org/2000/svg}svg'
    width, height = int(root.attrib['width']), int(root.attrib['height'])
    assert width > 0 and height > 0 and 'viewBox' in root.attrib
    for element in root.iter():
        tag = element.tag.rsplit('}', 1)[-1]
        assert tag not in {'script', 'foreignObject', 'image', 'animate', 'animateTransform'}
        for key, value in element.attrib.items():
            assert not key.lower().startswith('on')
            if key.rsplit('}', 1)[-1] in {'href', 'src'}:
                assert value.startswith('#'), 'No network references inside an SVG'
        if tag == 'text':
            assert 0 <= float(element.attrib['x']) <= width
            assert 0 <= float(element.attrib['y']) <= height
    print('PASS', name, 'XML, dimensions, alt text, public URL, and static content')
for url in re.findall(r'https://[^\s"<>\)]+', readme):
    assert urlparse(url).hostname in {'aozix.com', 'x.com', 'games.sshd.one', 'raw.githubusercontent.com'}
assert not re.search(r'(github_pat_|ghp_|sk-proj-|bu_)[A-Za-z0-9_-]{16,}', readme)
print('PASS English copy, official links, responsive pictures, and no private source links')
