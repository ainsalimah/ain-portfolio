"""Generate the local editorial social card (requires Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent.parent
image = Image.new('RGB', (1200, 630), '#f4f1e9')
draw = ImageDraw.Draw(image)
font = lambda size: ImageFont.truetype(str(root / 'assets/manrope.ttf'), size)

draw.line((65, 90, 1135, 90), fill='#c8cec3')
draw.text((65, 30), 'ain', font=font(42), fill='#202720')
draw.text((65, 135), 'PORTOFOLIO / FULL STACK DEVELOPER', font=font(16), fill='#a74728')
draw.text((60, 196), 'Empat produk.', font=font(82), fill='#202720')
draw.text((60, 298), 'Empat cerita.', font=font(82), fill='#a74728')
draw.text((875, 160), 'a', font=font(300), fill='#dfe3d7')
draw.line((65, 492, 1135, 492), fill='#c8cec3')
draw.text((65, 528), 'DevTrack  /  Stokita  /  Lumiere  /  Clinic Care', font=font(21), fill='#202720')
image.save(root / 'assets/social-card.png', optimize=True)
