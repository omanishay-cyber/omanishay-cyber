# Profile README: direction card

Local design note for the GitHub profile of omanishay-cyber.

## Brain inputs (2026-11-02)

- `brain taste`: owl-night palette loved, light river loved, Arno Pro and Verlag held as loved, editorial serif loved, still water that mirrors loved. A plainer page was rated 1.5 of 10: "you could have made this page 10million billion times better".
- `brain know find`: portfolio sections only, nothing on profile READMEs. `brain pages find`: no card fits. `brain assets find --kind sky`: HDR skies, not paintings; the paintings were made.
- `brain make hero` was refused (needs about 46 GB of commit, 38 GB free); `brain make art` at 1536 x 1024, then upscale x4.

## The card

- **Look:** Night Ledger, grown into a five-chapter catalogue of one maker's work. Painted landscapes, editorial serif, no badges, no glass.
- **Layout pattern:** a catalogue. A banner, then numbered chapters (I to V), each opening on the river band, then a cover, real text, then proof pictures.
- **Type:** Arno Pro Light Display and Light Italic Display for names and numbers; Verlag for labels and short lines. Baked text is at least 26 px in a 1000 px wide image, so it stays readable when the image is 358 px wide on a phone.
- **Palette:** dark ground `#080f1f`, ink `#f3f6fb`, gold `#f0c98a`; light ground `#eef2f7`, ink `#0b1730`, gold `#7c4d0c`. Tokens in `src/art.html`. No neon.
- **Signature:** the light river. A bundle of strands runs through every chapter band, and each band's right edge meets the next band's left edge.
- **Motion:** none. These are WebP stills on purpose: they cannot go blank in an off-screen image.
- **Paintings:** a lake with one lit tree and a bird (the banner: Stryx's tree and Perch's bird in one place), star trails over a standing stone (Mneme: a long exposure remembers every minute of the night).

Could this be any other developer's profile? No: the screens are Perch's and Stryx's own, and the paintings tie them together.

## Rebuild

From this folder's parent: `node design/src/render.cjs temp/png`, `python design/src/export.py`, `python design/src/build_readme.py`. Paintings and fonts live in the ignored `temp/art/`.
