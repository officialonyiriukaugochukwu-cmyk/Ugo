import re
import sys
sys.path.insert(0, "/home/user/Ugo/garabandal_visuals")
import common
import beats_a, beats_b, beats_c, beats_d  # noqa: F401  (import registers beats)
from common import BEATS, STYLE_IMG, STYLE_VID

WPS = 2.7


def norm(t):
    t = t.replace("“", '"').replace("”", '"').replace("’", "'")
    return re.sub(r"\s+", " ", t).strip()


# ---- coverage check against the master script ----
script = open("/home/user/Ugo/garabandal_script.md").read()
script_n = norm(script).replace("*", "")
joined = norm(" ".join(b["text"] for b in BEATS))
print("script words:", len(script_n.split()), "beat words:", len(joined.split()))
print("coverage exact:", joined == script_n)
if joined != script_n:
    a, b = script_n.split(), joined.split()
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            print("first mismatch at word", i, "|", " ".join(a[max(0, i - 6):i + 6]), "|||", " ".join(b[max(0, i - 6):i + 6]))
            break


def dur(text):
    return min(5.0, max(3.0, len(text.split()) / WPS))


out = []
out.append("# THE REAL REASON GARABANDAL WAS NEVER APPROVED — Visual Production Package\n")
out.append("**Style profile applied to every prompt:** Photorealistic documentary / archival live-action; muted desaturated "
           "documentary grade (cool grays, faded blacks, warm off-white paper) with sparse mustard-yellow or muted-red accents "
           "only on physical objects; available/practical light; locked-off or very slow observational camera; documents and "
           "objects dominate; high photorealism with 16mm grain; analytical, restrained, quietly ominous.\n")
out.append("**Production note:** The angel and the Virgin are never depicted. Apparition moments are shown only through "
           "the girls' faces, light on skin, and empty sky or ground. Real, named individuals are not depicted by likeness: "
           "the bishop, the friar, the girls, and the commission are generic period figures.\n")

cur = None
t = 0.0
n = 0
for b in BEATS:
    n += 1
    d = dur(b["text"])
    t += d
    if b["sec"] != cur:
        cur = b["sec"]
        out.append(f"\n---\n\n## {cur}\n")
    kind = "photorealistic archival still" if b["arch"] else "photorealistic documentary photograph"
    img = (f"A {kind}: {b['subj']}. {b['cam'].capitalize()}. Lighting: {b['light']}. Mood: {b['mood']}. "
           f"Moment: {b['action']}. {STYLE_IMG}")
    vid = (f"{STYLE_VID} {d:.1f} seconds. Scene: {b['subj']}. {b['motion']}. Camera: {b['cam']}. "
           f"Lighting: {b['light']}. Mood: {b['mood']}.")
    out.append(f"### Beat {n:03d} · ~{d:.1f}s\n")
    out.append(f"**[Script Segment Text]** {b['text']}\n")
    out.append(f"**Image Prompt:** {img}\n")
    out.append(f"**Camera Angle:** {b['cam']}\n")
    out.append(f"**Lighting:** {b['light']}\n")
    out.append(f"**Mood:** {b['mood']}\n")
    out.append(f"**Action:** {b['action']}\n")
    out.append(f"**Video Prompt:** {vid}\n")

mins, secs = divmod(int(round(len(script_n.split()) / WPS)), 60)
badge = f"{mins}:{secs:02d}"
print("beats:", n, "total approx runtime:", badge)

TH = f"""
---

## THUMBNAILS (5)

All thumbnails: 16:9, duration badge bottom-right reading **{badge}** in small white sans-serif on a dark rounded rectangle.
Photorealistic documentary photographs; bold oversized condensed display type, 2 lines max; one dominant muted hue behind high-contrast text.

### Thumbnail 1 — The Stamp
- **Visual concept:** Tight, off-center photograph of an aged hand holding a wooden-handled rubber stamp inches above a typed Latin page, the stamp not touching the paper; negative space on the page for text.
- **Text overlay:** NOT APPROVED. / NOT BANNED.
- **Emotion trigger:** Institutional tension and withheld judgment.
- **Image prompt:** A photorealistic documentary photograph of an aged male hand with a plain gold ring holding a wooden-handled rubber stamp with muted red ink a few centimeters above a typed carbon-copy Latin document on warm off-white paper, the stamp not touching the page, the hand and stamp placed in the right third of the frame with generous negative space on the left, a mustard-yellow paper clip at the page corner, dark wooden desk, green-shaded brass desk lamp light with gentle falloff, 16mm film grain, muted desaturated documentary grade dominated by cool gray-green tones, tense and restrained, not an illustration, not glossy.

### Thumbnail 2 — The Date
- **Visual concept:** Extreme close-up of a paper wall calendar with a single date circled in muted red grease pencil, numeral blurred, off-center, shallow depth of field.
- **Text overlay:** THE DATE / NOBODY KNOWS
- **Emotion trigger:** Curiosity gap and quiet dread.
- **Image prompt:** A photorealistic documentary photograph of an old paper wall calendar page with one square circled in muted red grease pencil, the numeral inside out of focus, the circle placed in the left third of the frame, shallow depth of field, warm off-white aged paper with visible fiber and a pinhole at the top, soft window light from one side, 16mm film grain, muted desaturated grade dominated by cool slate-blue gray, expectant and quietly ominous, not an illustration, not glossy.

### Thumbnail 3 — The Girl
- **Visual concept:** Tight portrait of a twelve-year-old girl in 1961 village clothing, head tilted back, eyes fixed on empty dark sky, flashlight glow on her face, unsmiling, off-center with negative space for text.
- **Text overlay:** SHE NEVER / LOOKED BEHIND
- **Emotion trigger:** Uncanny underdog; direct unsettled gaze energy.
- **Image prompt:** A photorealistic archival still of a twelve-year-old Spanish village girl in 1961 in a dark wool cardigan with two plain braids, her chin lifted and eyes wide and unblinking fixed on the dark sky above the camera, harsh handheld flashlight glow from below left on her skin, deep black night background with rocky ground barely visible, face placed in the right third of the frame, 16mm film grain, muted desaturated grade dominated by cool charcoal gray, uncanny and restrained, natural skin texture, not an illustration, not glossy.

### Thumbnail 4 — The Case File
- **Visual concept:** Thick tied case folder labeled GARABANDAL with a muted-red UNPROVEN stamp, shot from a low angle on a dark desk, folder off-center.
- **Text overlay:** 60 YEARS. / NO VERDICT.
- **Emotion trigger:** Institutional tension and long suspension.
- **Image prompt:** A photorealistic documentary photograph of a thick manila case folder tied with string, a typed label reading GARABANDAL, a muted-red rubber-stamp mark reading UNPROVEN across the cover, yellowed edges, mustard-yellow paper clip, lying on a dark wooden desk shot from a low angle, folder placed in the left third of the frame with dark negative space on the right, green-shaded desk lamp light with gentle falloff and dust motes, 16mm film grain, muted desaturated grade dominated by deep cool gray-brown, heavy and analytical, not an illustration, not glossy.

### Thumbnail 5 — The Unsigned Letter
- **Visual concept:** Aged hand of a brown-habited friar (face out of frame) holding a letter whose signature line is blank, off-center.
- **Text overlay:** THE LETTER / NOBODY SIGNED
- **Emotion trigger:** Doubt and institutional ambiguity.
- **Image prompt:** A photorealistic documentary photograph of the aged hand and coarse brown wool sleeve of a Capuchin friar with a white rope cord holding a typed letter on thin off-white paper whose signature line at the bottom is blank, face out of frame, the letter placed in the right third of the frame with negative space on the left, soft window light from the left with gentle falloff, a faint mustard-yellow pencil underline on the blank signature line, 16mm film grain, muted desaturated grade dominated by warm gray-brown, ambiguous and quietly ominous, not an illustration, not glossy.
"""
out.append(TH)
open("/home/user/Ugo/garabandal_visuals/garabandal_visual_package.md", "w").write("\n".join(out))
print("words in package:", len(" ".join(out).split()))
