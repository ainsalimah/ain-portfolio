"""Render static project content from projects.json. No dependencies required."""
import json
from hashlib import sha256
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
ICONS = {
    'board': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16m6-16v16M5.5 8h1M11.5 8h1M17.5 8h1M5.5 12h1m5 0h1m5 0h1"/>',
    'clinic': '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
    'chair': '<path d="M6 13V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8M4 11v6h16v-6M6 17v4m12-4v4M6 13h12"/>',
    'stock': '<path d="m12 2 8 4.5v9L12 20l-8-4.5v-9L12 2Zm0 9L4 6.5m8 4.5 8-4.5M12 11v9M8 4.3l8 4.5M2 20h4m12 0h4"/>',
    'arrow': '<path d="M5 19 19 5M5 5h14v14"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
def render(p):
    e = lambda k: escape(p[k], quote=True)
    tags = ''.join(f'<li>{escape(tag)}</li>' for tag in p['tags'])
    sections = ''.join(f'<div><h4>{label}</h4><p>{e(key)}</p></div>' for label, key in [('Masalah yang diselesaikan','problem'),('Alur utama','flow'),('Keputusan teknis','decisions'),('Batasan proyek','limits')])
    return f'''<article class="project reveal" id="{e('id')}">
      <div class="project-top"><span class="project-index">/{e('number')}</span><span class="eyebrow">{e('category')}</span><span class="project-symbol">{icon(p['icon'])}</span></div>
      <div class="project-grid">
        <div class="project-visual {e('tone')}"><div class="visual-orbit" aria-hidden="true"></div><div class="browser-frame"><div class="browser-bar" aria-hidden="true"><i></i><i></i><i></i><span>{escape(p['demo'].split('//')[1].rstrip('/'))}</span></div><img src="assets/{e('image')}" width="1440" height="1000" alt="{e('alt')}" loading="lazy"></div><span class="visual-caption">{e('caption')}</span></div>
        <div class="project-copy"><h3>{e('name')}</h3><p class="project-headline">{e('headline').replace(chr(10), '<br>')}</p><p class="description">{e('description')}</p><ul class="tags" aria-label="Teknologi {e('name')}">{tags}</ul><div class="project-links"><a class="text-link" href="{e('demo')}" target="_blank" rel="noopener noreferrer">Lihat demo {icon('arrow')}<span class="sr-only"> {e('name')} (tab baru)</span></a><a class="source-link" href="{e('github')}" target="_blank" rel="noopener noreferrer">Kode sumber<span class="sr-only"> {e('name')} (tab baru)</span></a></div></div>
      </div>
      <details class="case-study"><summary><span>Di balik {e('name')}</span><span class="summary-label">STUDI KASUS <span class="plus" aria-hidden="true">+</span></span></summary><div class="case-content">{sections}</div></details>
    </article>'''
projects = json.loads((ROOT / 'projects.json').read_text(encoding='utf-8'))
template = (ROOT / 'template.html').read_text(encoding='utf-8')
for asset, attribute in [('styles.css', 'href'), ('app.js', 'src')]:
    version = sha256((ROOT / asset).read_bytes()).hexdigest()[:12]
    template = template.replace(f'{attribute}="{asset}"', f'{attribute}="{asset}?v={version}"')
(ROOT / 'index.html').write_text(template.replace('<!-- PROJECTS -->', '\n'.join(map(render, projects))), encoding='utf-8')
print(f'Built index.html: {len(projects)} projects, readable without JavaScript.')
