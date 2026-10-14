"""Generate the local social sharing artwork (Pillow needed only to regenerate)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent.parent
im = Image.new('RGB', (1200, 630), '#151515')
d = ImageDraw.Draw(im)
font = lambda size: ImageFont.truetype(str(root / 'assets/manrope.ttf'), size)
d.line((65, 90, 1135, 90), fill='#383630')
d.text((65, 30), 'ain', font=font(42), fill='#F3EFE6')
d.text((65, 135), 'PORTOFOLIO / FULL STACK DEVELOPER', font=font(16), fill='#C49A6C')
d.text((60, 196), 'Dari ide,', font=font(82), fill='#F3EFE6')
d.text((60, 298), 'menjadi aplikasi.', font=font(82), fill='#C49A6C')
for inset in range(0, 100, 20):
    d.ellipse((880+inset, 145, 1150-inset, 435), outline='#C49A6C', width=1)
d.line((65, 492, 1135, 492), fill='#383630')
d.text((65, 528), 'DevTrack   /   Stokita   /   Lumiere', font=font(22), fill='#F3EFE6')
d.text((945, 536), 'Ain · 2026', font=font(18), fill='#C49A6C')
im.save(root / 'assets/social-card.png', optimize=True)
