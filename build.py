"""src/ -> pagina pronta per l'import da URL in CheckoutChamp.
URL assoluti e CSS esterno con hash nel nome (CC non sovrascrive file con lo stesso nome)."""
import hashlib, glob, os, re
ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://camillithomas7-prog.github.io/avera-stride/'
css = open(f'{ROOT}/src/style.css').read().replace('ASSETS/', BASE + 'assets/')
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S); css = re.sub(r'\s*\n\s*', '', css)
v = hashlib.md5(css.encode()).hexdigest()[:8]
for old in glob.glob(f'{ROOT}/style-*.css'): os.remove(old)
open(f'{ROOT}/style-{v}.css', 'w').write(css)
html = open(f'{ROOT}/src/index.html').read().replace('ASSETS/', BASE + 'assets/').replace('STYLE', f'{BASE}style-{v}.css')
html = html.encode('ascii', 'xmlcharrefreplace').decode()  # niente caratteri non ASCII per l'importer CC
assert not re.search(r'="[^"]*<[^"]*"', html), "'<' dentro un attributo"
open(f'{ROOT}/index.html', 'w').write(html)
# anteprima locale con percorsi relativi
open(f'{ROOT}/preview.html', 'w').write(open(f'{ROOT}/src/index.html').read().replace('ASSETS/', 'assets/').replace('STYLE', 'preview.css'))
open(f'{ROOT}/preview.css', 'w').write(open(f'{ROOT}/src/style.css').read().replace('ASSETS/', 'assets/'))
print('html', len(html), 'css', len(css), f'style-{v}.css')
