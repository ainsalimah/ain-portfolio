"""Build the static portfolio and four project case studies from projects.json."""
import json
from hashlib import sha256
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = json.loads((ROOT / 'projects.json').read_text(encoding='utf-8'))
TECH = [
    ('React', 'react'), ('TypeScript', 'typescript'), ('Next.js', 'nextjs'),
    ('Node.js', 'nodejs'), ('PostgreSQL', 'postgresql'), ('Prisma', 'prisma'),
    ('PHP', 'php'), ('MySQL', 'mysql'), ('Python', 'python'),
]
ICONS = {name: slug for name, slug in TECH}
ICONS['Express'] = 'express'


def e(value):
    return escape(str(value), quote=True)


def asset(path, depth=0):
    return f"{'../' * depth}assets/{e(path)}"


def tech_icon(name, depth=0):
    slug = ICONS.get(name)
    if not slug:
        return ''
    return f'<img src="{asset(f"icons/{slug}.svg", depth)}" width="22" height="22" alt="" loading="lazy">'


def tech_list(tags, depth=0):
    return ''.join(f'<li>{tech_icon(tag, depth)}<span>{e(tag)}</span></li>' for tag in tags)


def project_card(project):
    p = project
    return f'''<article class="project reveal" id="{e(p['id'])}">
      <div class="project-top"><span class="project-index">{e(p['number'])} / 04</span><span class="eyebrow">{e(p['category'])}</span></div>
      <div class="project-grid">
        <a class="project-visual {e(p['tone'])}" href="projects/{e(p['id'])}/" aria-label="Baca studi kasus {e(p['name'])}"><img src="{asset(p['image'])}" width="1440" height="1000" alt="{e(p['alt'])}" loading="lazy"><span class="visual-caption">{e(p['caption'])}</span></a>
        <div class="project-copy"><p class="project-kicker">PROYEK PILIHAN — {e(p['number'])}</p><h3>{e(p['name'])}</h3><p class="project-headline">{e(p['headline']).replace(chr(10), '<br>')}</p><p class="description">{e(p['description'])}</p><div class="project-stack"><span>TEKNOLOGI UTAMA</span><ul class="tags" aria-label="Teknologi {e(p['name'])}">{tech_list(p['tags'])}</ul></div><div class="project-links"><a class="text-link" href="projects/{e(p['id'])}/">Baca studi kasus <span aria-hidden="true">↗</span></a><a class="source-link" href="{e(p['demo'])}" target="_blank" rel="noopener noreferrer">Coba aplikasi <span aria-hidden="true">↗</span><span class="sr-only"> {e(p['name'])} (tab baru)</span></a></div></div>
      </div>
    </article>'''


def detail_page(project, next_project, styles_version, script_version):
    p = project
    gallery = ''.join(f'''<figure class="story-step reveal"><div class="story-number">{index:02d} / {len(p['gallery']):02d}</div><a class="story-image {e(p['tone'])}" href="{asset(item['image'], 2)}" target="_blank" rel="noopener noreferrer" aria-label="Buka gambar penuh: {e(item['title'])}"><img src="{asset(item['image'], 2)}" alt="{e(item['alt'])}" loading="lazy"></a><figcaption><h3>{e(item['title'])}</h3><p>{e(item['caption'])}</p><a class="image-link" href="{asset(item['image'], 2)}" target="_blank" rel="noopener noreferrer">Lihat gambar penuh ↗<span class="sr-only"> (tab baru)</span></a></figcaption></figure>''' for index, item in enumerate(p['gallery'], 1))
    next_link = f'<a class="next-project" href="../{e(next_project["id"])}/"><span>PROYEK BERIKUTNYA</span><strong>{e(next_project["name"])}</strong><span aria-hidden="true">↗</span></a>'
    return f'''<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(p['name'])} — Studi Kasus | Ain</title>
  <meta name="description" content="Studi kasus {e(p['name'])}: {e(p['description'])}">
  <meta name="theme-color" content="#f4f1e9">
  <link rel="canonical" href="https://ain-portfolio-zeta.vercel.app/projects/{e(p['id'])}/">
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="../../assets/manrope.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="stylesheet" href="../../styles.css?v={styles_version}"><script defer src="../../app.js?v={script_version}"></script>
</head>
<body>
  <a class="skip-link" href="#main">Lewati ke konten utama</a>
  <header class="site-header wrap"><a class="wordmark" href="../../" aria-label="Ain, kembali ke beranda">ain<span aria-hidden="true">✳</span></a><nav aria-label="Navigasi utama"><a href="../../#proyek">Semua proyek <span>04</span></a><a href="../../#tentang">Tentang</a><a href="../../#kontak" class="nav-contact">Kontak <span aria-hidden="true">↗</span></a></nav></header>
  <main id="main" class="detail-main">
    <div class="wrap detail-breadcrumb"><a href="../../#proyek">← Semua proyek</a><span>{e(p['number'])} / 04</span></div>
    <section class="detail-hero wrap" aria-labelledby="detail-title"><p class="eyebrow">STUDI KASUS / {e(p['category'])}</p><div class="detail-hero-grid"><div><h1 id="detail-title">{e(p['name'])}<span class="title-period">.</span></h1><p class="detail-lead">{e(p['headline']).replace(chr(10), '<br>')}</p></div><div class="detail-hero-side"><p>{e(p['description'])}</p><ul class="tags" aria-label="Teknologi {e(p['name'])}">{tech_list(p['tags'], 2)}</ul><div class="detail-actions"><a class="button" href="{e(p['demo'])}" target="_blank" rel="noopener noreferrer">Coba aplikasi <span aria-hidden="true">↗</span><span class="sr-only"> (tab baru)</span></a><a class="subtle-link" href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">Lihat kode ↗<span class="sr-only"> (tab baru)</span></a></div></div></div></section>
    <div class="wrap"><figure class="detail-cover {e(p['tone'])}"><img src="{asset(p['image'], 2)}" alt="{e(p['alt'])}" fetchpriority="high"><figcaption>{e(p['caption'])}</figcaption></figure></div>
    <section class="detail-intro wrap" aria-labelledby="challenge-title"><div><p class="eyebrow">01 / KONTEKS</p><h2 id="challenge-title">Masalah yang<br><em>dipecahkan.</em></h2></div><p>{e(p['problem'])}</p></section>
    <section class="detail-story wrap" aria-labelledby="story-title"><div class="section-heading"><div><p class="eyebrow">02 / PRODUK</p><h2 id="story-title">Lihat alurnya,<br><em>langkah demi langkah.</em></h2></div><p>{e(p['flow'])}</p></div><div class="story-list">{gallery}</div></section>
    <section class="detail-notes" aria-label="Keputusan dan batasan proyek"><div class="wrap notes-grid"><div><p class="eyebrow">03 / DI BALIK LAYAR</p><h2>Yang membuatnya<br><em>bekerja.</em></h2></div><div class="note-list"><article><span>01</span><div><h3>Keputusan teknis</h3><p>{e(p['decisions'])}</p></div></article><article><span>02</span><div><h3>Catatan demo</h3><p>{e(p['limits'])}</p></div></article></div></div></section>
    <div class="wrap detail-end"><a class="text-link" href="../../#proyek">← Kembali ke semua proyek</a>{next_link}</div>
  </main>
  <footer class="site-footer wrap"><a class="wordmark" href="../../" aria-label="Kembali ke beranda">ain<span aria-hidden="true">✳</span></a><p>Portofolio Ain · 2026</p><div><button id="motion-toggle" type="button" aria-pressed="false" hidden>Jeda animasi</button><a href="../../#kontak">Kontak ↗</a></div></footer>
</body></html>'''


template = (ROOT / 'template.html').read_text(encoding='utf-8')
def version(path):
    # Git may check out CRLF on Windows; asset URLs should be stable across platforms.
    normalized = (ROOT / path).read_text(encoding='utf-8').replace('\r\n', '\n')
    return sha256(normalized.encode('utf-8')).hexdigest()[:12]


styles_version = version('styles.css')
script_version = version('app.js')
template = template.replace('href="styles.css"', f'href="styles.css?v={styles_version}"')
template = template.replace('src="app.js"', f'src="app.js?v={script_version}"')
tech_strip = ''.join(f'<span class="tech-item">{tech_icon(name)}<span>{e(name)}</span></span>' for name, _ in TECH)
homepage = template.replace('<!-- TECH -->', tech_strip).replace('<!-- PROJECTS -->', '\n'.join(map(project_card, PROJECTS)))
(ROOT / 'index.html').write_text(homepage, encoding='utf-8')

for index, project in enumerate(PROJECTS):
    destination = ROOT / 'projects' / project['id']
    destination.mkdir(parents=True, exist_ok=True)
    next_project = PROJECTS[(index + 1) % len(PROJECTS)]
    (destination / 'index.html').write_text(detail_page(project, next_project, styles_version, script_version), encoding='utf-8')

print(f'Built index.html and {len(PROJECTS)} case studies; all content works without JavaScript.')
