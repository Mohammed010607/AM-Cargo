"""Produce artifact.html from index.html.

The artifact host wraps whatever it is given in its own <!doctype>/<html>/
<head>/<body>, so the page has to be handed over without one. Everything else
- the title, the font link, the stylesheet and the markup - is carried across
unchanged, and the media is published alongside from media/.

    python build-artifact.py
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'index.html')
OUT = os.path.join(HERE, 'artifact.html')

TITLE = 'AM Cargo'

s = io.open(SRC, encoding='utf-8').read()

head = s[s.index('<head>') + len('<head>'):s.index('</head>')]
body = s[s.index('<body>') + len('<body>'):s.index('</body>')]

fonts = '\n'.join(re.findall(r'<link rel="[^"]*(?:preconnect|stylesheet)"[^>]*>', head))
style = head[head.index('<style>'):head.index('</style>') + len('</style>')]

page = f'<title>{TITLE}</title>\n{fonts}\n{style}\n{body.strip()}\n'

for tag in ('<!doctype', '<html', '<head>', '<body>'):
    assert tag not in page.lower(), f'{tag} survived into the output'

io.open(OUT, 'w', encoding='utf-8').write(page)
print(f'artifact.html written, {len(page):,} chars')
print('media referenced:', ', '.join(sorted(set(re.findall(r'media/[\w.-]+', page)))))
