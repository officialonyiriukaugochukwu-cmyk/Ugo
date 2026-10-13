"""Shared constants and helper for the Garabandal visual package."""

STYLE_IMG = (
    "Shot as 16mm documentary film with subtle film grain; muted desaturated documentary grade of cool grays, "
    "faded blacks and warm off-white paper tones; natural skin and fabric texture, visible paper fiber, dust and age; "
    "documentary framing with generous negative space; not an illustration, not halftone, not cartoon, not glossy or commercial."
)
STYLE_VID = (
    "Photorealistic live-action documentary footage, 16mm film grain, muted desaturated documentary grade "
    "(cool grays, faded blacks, warm off-white paper tones), restrained observational motion, no stylized or graphic movement."
)

# ---- recurring elements (fully re-described in every prompt that uses them) ----
GIRL = ("a twelve-year-old Spanish village girl in 1961, dark wool cardigan over a plain cotton dress, dark stockings, "
        "black leather shoes, hair in two plain braids")
GIRLS4 = ("four village girls aged eleven to twelve in 1961, each in a dark wool cardigan over a plain cotton dress, "
          "dark stockings and plain braids")
PATH = "a steep mountain path of loose gray limestone rocks and sparse grass above a Cantabrian hamlet at night"
ADULTS = ("village farmers in dark wool jackets and flat caps, a physician in a dark overcoat carrying a leather bag, "
          "and priests in black cassocks")
VILL = ("the stone hamlet of San Sebastian de Garabandal in Cantabria, Spain, 1961: gray stone farmhouses with weathered "
        "red-clay tile roofs, a rutted dirt track, steep green mountain slopes under an overcast sky")
CHURCH = "the small plain stone parish church of the hamlet with a squat bell tower and a weathered wooden door"
MOTHER = "a widowed Spanish village mother in a black dress and black headscarf, work-worn hands"
ORCH = "a walled apple orchard on a stone-terraced hillside in summer, green apples on the branches"
OFFICE = ("a 1960s Spanish diocesan office: dark carved wooden desk, brass desk lamp with a green glass shade, "
          "whitewashed wall with a plain wooden crucifix, stacked cardboard folders tied with string, a manual typewriter")
DOCLAT = "a typed carbon-copy Latin document on warm off-white paper, ink absorbed into visible paper fiber, faint creases"
STAMP = "a wooden-handled rubber stamp with muted red ink, pad beside it"
COMM = ("a long dark wooden table at which four priests in black clerical suits and one physician in a gray suit sit, "
        "open notebooks and a glass water carafe before them, 1962")
CROWD = ("a crowd of several hundred villagers and visitors in dark 1960s wool coats and headscarves gathered on a stony "
         "hillside at dusk, mostly seen from behind")
PINES = "a small grove of pine trees on a rocky hillside above the hamlet, rough bark, bare stony ground, overcast sky"
BISHOP = ("an elderly Spanish bishop in a black cassock with purple piping and a pectoral cross, aged hands, "
          "face partly turned from the camera")
FRIAR = "a Capuchin friar in a coarse brown habit with a white rope cord, aged hands, face turned away from the camera"
MODERN = ("a modern Vatican-style administrative office: pale wood desk, overhead fluorescent panels, a printed multi-page "
          "document with one line marked by a mustard-yellow highlighter, a plain stapled stack of papers, a closed laptop")
FOLDER = "a manila case folder with a typed label, yellowed edges and a mustard-yellow paper clip"

# ---- lighting / mood shorthands ----
LN = "handheld flashlight beams from off-frame in darkness, deep shadows, gentle falloff"
LD = "soft overcast daylight, flat with gentle falloff"
LK = "a single green-shaded brass desk lamp plus pale window light, gentle falloff"
LF = "overhead institutional fluorescents, flat even light"
LW = "soft window light from one side, gentle falloff"
LC = "dim candlelight and a single practical lamp, low contrast"
LE = "low evening sun through haze, flat and muted"

BEATS = []
CURSEC = [""]


def S(name):
    CURSEC[0] = name


def B(text, subj, cam, light, mood, action, motion, arch=False):
    """Register one beat. arch=True marks it as a treated archival still."""
    BEATS.append(dict(sec=CURSEC[0], text=text, subj=subj, cam=cam, light=light, mood=mood,
                      action=action, motion=motion, arch=arch))
