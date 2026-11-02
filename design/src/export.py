"""Turn the rendered PNGs into assets/*.webp, copy the reused Perch and Stryx art, and measure text contrast on the bare renders."""
import glob, json, os, re, shutil, sys
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PNG = os.path.join(ROOT, 'temp', 'png')
ASSETS = os.path.join(ROOT, 'assets')
PERCH = 'D:/PROJECTS/perch-site/docs/assets/readme/'
STRYX = 'D:/PROJECTS/stryx-skills-page/release/repo-init/docs/assets/readme/'
NAMES = {'ch1': 'ch1', 'ch2': 'ch2', 'ch3': 'ch3', 'ch4': 'ch4', 'ch5': 'ch5', 'banner': 'banner', 'perchnums': 'perch-nums',
         'mosaic': 'perch-mosaic', 'mneme': 'mneme-cover', 'mneask': 'mneme-ask', 'mnecold': 'mneme-cold', 'craft': 'craft', 'closing': 'closing'}
Q = {'banner': 82, 'mneme-cover': 80}
os.makedirs(ASSETS, exist_ok=True)


def save(im, name, q=80, w=2000):
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(os.path.join(ASSETS, name + '.webp'), 'WEBP', quality=q, method=6)


for src, dst in NAMES.items():
    for t in ('dark', 'light'):
        p = os.path.join(PNG, f'{src}-{t}.png')
        if os.path.exists(p):
            save(Image.open(p), f'{dst}-{t}', Q.get(dst, 76))
for b in ('btn-perch', 'btn-stryx', 'btn-mneme'):
    p = os.path.join(PNG, f'{b}-dark.png')
    if os.path.exists(p):
        save(Image.open(p), b, 86)

# reused art, as WebP, in this repo
PAIRS = [(PERCH + 'b-banner.webp', PERCH + 'b-banner-light.webp', 'perch-cover'), (PERCH + 'b-notch.webp', PERCH + 'b-notch-light.webp', 'perch-notch'),
         (PERCH + 'b-dock.webp', PERCH + 'b-dock-light.webp', 'perch-dock'), (STRYX + 'hero-dark.webp', STRYX + 'hero-light.webp', 'stryx-hero'),
         (STRYX + 'features-1-dark.webp', STRYX + 'features-1-light.webp', 'stryx-f1'), (STRYX + 'features-2-dark.webp', STRYX + 'features-2-light.webp', 'stryx-f2'),
         (STRYX + 'features-3-dark.webp', STRYX + 'features-3-light.webp', 'stryx-f3'), (STRYX + 'flow-dark.webp', STRYX + 'flow-light.webp', 'stryx-flow')]
for d, l, n in PAIRS:
    for src, t in ((d, 'dark'), (l, 'light')):
        im = Image.open(src)
        if im.width <= 2000:   # already the right size: the same bytes, no second lossy pass
            shutil.copyfile(src, os.path.join(ASSETS, f'{n}-{t}.webp'))
        else:
            save(im, f'{n}-{t}', 78)
shutil.copyfile(PERCH + 'z-start.webp', os.path.join(ASSETS, 'perch-start.webp'))

# measured contrast: each text box against the worst pixel of the same box with the text hidden
def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])
def ratio(a, b):
    la, lb = max(a, b), min(a, b)
    return (la + 0.05) / (lb + 0.05)

GH = {'dark': (13, 17, 23), 'light': (255, 255, 255)}
boxes = json.load(open(os.path.join(PNG, 'boxes.json')))
worst = []
for key, items in boxes.items():
    theme = key.rsplit('-', 1)[1]
    im = Image.open(os.path.join(PNG, key + '.bare.png')).convert('RGBA')
    bg = Image.new('RGBA', im.size, GH[theme] + (255,))
    bg.alpha_composite(im)
    px = bg.convert('RGB')
    for it in items:
        m = re.findall(r'[\d.]+', it['color'])
        ink = lum([float(v) for v in m[:3]])
        box = (max(0, int(it['x'] * 2)), max(0, int(it['y'] * 2)), min(px.width, int((it['x'] + it['w']) * 2)), min(px.height, int((it['y'] + it['h']) * 2)))
        if box[2] <= box[0] or box[3] <= box[1]:
            continue
        data = sorted(lum(p) for p in px.crop(box).resize((60, 16)).get_flattened_data())
        # 2nd percentile on the side that is closest to the ink, so one star does not decide
        closest = min(ratio(ink, data[int(len(data) * 0.98)]), ratio(ink, data[int(len(data) * 0.02)]))
        worst.append((round(closest, 2), key, it['t'], it['px']))
worst.sort()
for w in worst[:18]:
    print(w)
print('text boxes measured', len(worst), 'under 4.5:', sum(1 for w in worst if w[0] < 4.5))
total = sum(os.path.getsize(f) for f in glob.glob(ASSETS + '/*.webp'))
print('assets', len(glob.glob(ASSETS + '/*.webp')), 'files', round(total / 1e6, 2), 'MB')
