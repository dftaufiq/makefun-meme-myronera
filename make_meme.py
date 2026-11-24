from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = 'media-generation-meme-agent-3am-0-78d47418-433d-4b40-b02c-745e71b4d8ff.png'
OUT = 'meme.png'
W = 1080
im = Image.open(SRC).convert('RGB').resize((W, W), Image.LANCZOS)
overlay = Image.new('RGBA', (W, W), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
# top scrim (dark gradient)
for y in range(0, 250):
    a = int(190 * (1 - y / 250) ** 1.2)
    od.line([(0, y), (W, y)], fill=(0, 0, 0, a))
# bottom scrim
for y in range(W - 360, W):
    a = int(200 * ((y - (W - 360)) / 360) ** 1.2)
    od.line([(0, y), (W, y)], fill=(0, 0, 0, a))
im = Image.alpha_composite(im.convert('RGBA'), overlay).convert('RGB')
d = ImageDraw.Draw(im)

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def text_block(lines, y0, size, fill, stroke_w):
    font = ImageFont.truetype(FONT, size)
    # shrink until widest line fits
    while True:
        ws = [d.textlength(t, font=font) for t in lines]
        if max(ws) <= W - 70 or size <= 30:
            break
        size -= 2
        font = ImageFont.truetype(FONT, size)
    y = y0
    for t in lines:
        w = d.textlength(t, font=font)
        d.text(((W - w) / 2, y), t, font=font, fill=fill,
               stroke_width=stroke_w, stroke_fill=(0, 0, 0))
        y += int(size * 1.12)
    return y

# Top: setup (white)
text_block(['ME: JUST ONE BOUNTY,', 'THEN WE SLEEP'], 34, 74, (255, 255, 255), 4)
# Bottom: reveal (yellow)
text_block(['MY AGENT AT 3AM:', '47 ENTRIES. $0.60 RICHER.', 'STILL BUILDING.'], 724, 62, (255, 214, 10), 4)

im.save(OUT, 'PNG')
print('saved', OUT, im.size)
# 300px legibility check render
im.resize((300, 300), Image.LANCZOS).save('meme-300px-check.png')
print('saved 300px check')
