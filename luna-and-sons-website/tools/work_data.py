"""
Project photo catalogue for the Our Work gallery (and the homepage teaser).

To add a photo: put the file anywhere under the site folder, add one entry to
_WORK below, then run
    python3 tools/build_work.py && python3 tools/build_home.py
Photos are never edited, resized or recolored — the page links the original
files. Only photos of Luna & Sons' own completed projects belong here.

Entry: (path relative to the site root, category, alt_en, alt_es)
Categories: patios | walls | planting

Deliberately NOT listed (not completed-project photos):
  - luna photos/*.png renderings & plans (design, consulting, build and transform, pic 10-12)
  - luna photos/pic 2 (trailer), pic 9 (crew member) — brand photos, not projects
  - images/luna photos/unnamed-*.png — full-size originals of the images/luna-sons-*.jpg files below
  - landscape images/IMG_3039.JPG — same photo as images/new-gallery/IMG_3725.jpeg
  - images/luna-sons-retaining-wall-02.jpg — near-duplicate view of retaining-wall-01
"""
import os

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIES = [
    ("patios", "Outdoor Living & Patios", "Vida al Aire Libre y Patios"),
    ("walls", "Walls & Hardscape", "Muros y Hardscape"),
    ("planting", "Planting & Turf", "Plantación y Césped"),
]

NG = "images/new-gallery/"
LI = "landscape images/"

_WORK = [
    # ---- Outdoor Living & Patios
    (NG + "IMG_3708.JPEG", "patios",
     "Wood pergola over a large paver patio, with a planting bed, lawn and wood fence behind",
     "Pérgola de madera sobre un amplio patio de adoquines, con jardinera, césped y cerca de madera al fondo"),
    ("images/luna-sons-pergola-01.jpg", "patios",
     "Hardtop gazebo over a patio with outdoor seating, a stone planter wall, junipers and gravel beds",
     "Cenador con techo sólido sobre un patio con asientos exteriores, muro jardinera de piedra, enebros y camas de grava"),
    (NG + "IMG_3709.jpeg", "patios",
     "Curved paver patio with a low stone seat wall, a planted bed and a path light",
     "Patio curvo de adoquines con un muro bajo de piedra, una jardinera y una luz de sendero"),
    ("images/luna-sons-flagstone-patio-01.jpg", "patios",
     "Flagstone patio curving around a red maple toward a garden shed and wood deck",
     "Patio de piedra laja que rodea un arce rojo hacia una caseta de jardín y una terraza de madera"),
    (NG + "IMG_3725.jpeg", "patios",
     "Curving flagstone patio and walkway beside a mulched planting bed, with yellow flowers in the foreground and a pasture beyond",
     "Patio y sendero curvos de piedra laja junto a una jardinera con mantillo, con flores amarillas al frente y un pastizal al fondo"),
    ("images/luna-sons-flagstone-patio-02.jpg", "patios",
     "Flagstone stepping area with a yellow bistro table beside a boulder rock feature",
     "Área de piedra laja con una mesa de bistró amarilla junto a un elemento decorativo de rocas"),
    ("images/luna-sons-paver-patio-02.jpg", "patios",
     "Paver patio with an outdoor dining set beside a gray home",
     "Patio de adoquines con un comedor exterior junto a una casa gris"),
    ("images/luna-sons-paver-patio-01.jpg", "patios",
     "Paver patio with a dining set, seen from the yard",
     "Patio de adoquines con un comedor exterior, visto desde el jardín"),
    (LI + "IMG_3057.jpeg", "patios",
     "Flagstone path winding through a courtyard garden beside a tile-roof home",
     "Sendero de piedra laja que serpentea por un jardín interior junto a una casa con techo de teja"),
    (LI + "IMG_3051.jpeg", "patios",
     "Square gray paver patio in a side yard beside a white fence",
     "Patio de adoquines cuadrados grises en un patio lateral junto a una cerca blanca"),
    (LI + "IMG_3049.jpeg", "patios",
     "Gray paver patio beside a home entry with a dark gate",
     "Patio de adoquines grises junto a la entrada de una casa con un portón oscuro"),
    (LI + "IMG_3068.jpeg", "patios",
     "Backyard with a curved turf lawn, concrete patio, dining set and orange umbrella",
     "Patio trasero con césped curvo, patio de concreto, comedor y sombrilla naranja"),

    # ---- Walls & Hardscape
    (NG + "IMG_3706.JPEG", "walls",
     "Terraced block retaining walls with planted slopes, young trees and a turf lawn beside a dark ranch fence",
     "Muros de contención de bloque en terrazas con taludes plantados, árboles jóvenes y césped junto a una cerca oscura"),
    (NG + "IMG_3707.JPEG", "walls",
     "Gray paver driveway beside a garage with a low redwood fence",
     "Entrada de adoquines grises junto a un garaje con una cerca baja de secoya"),
    (NG + "IMG_3710.jpeg", "walls",
     "Curved block retaining wall with a capstone above beds of river rock",
     "Muro de contención curvo de bloque con remate superior sobre camas de piedra de río"),
    ("images/luna-sons-retaining-wall-01.jpg", "walls",
     "Curved segmental block planters framing a brick-home entry",
     "Jardineras curvas de bloque enmarcando la entrada de una casa de ladrillo"),
    ("images/luna-sons-retaining-wall-04.jpg", "walls",
     "Curved stone planter walls and a gravel entry path in front of a stone-and-timber home",
     "Muros jardinera curvos de piedra y un sendero de grava frente a una casa de piedra y madera"),
    ("images/luna-sons-retaining-wall-03.jpg", "walls",
     "Curved stone retaining wall planter with flowering shrubs above a turf lawn",
     "Jardinera curva con muro de piedra y arbustos en flor sobre un césped"),
    ("images/luna-sons-paver-walkway-01.jpg", "walls",
     "Square concrete paver walkway set in river rock along a side-yard fence",
     "Camino de adoquines de concreto cuadrados sobre piedra de río junto a una cerca lateral"),
    ("images/luna-sons-retaining-wall-06.jpg", "walls",
     "Turf side yard bordered by a low block wall and a wood fence",
     "Patio lateral con césped delimitado por un muro bajo de bloque y una cerca de madera"),
    (LI + "IMG_3056.jpeg", "walls",
     "Concrete stepping-stone walkway between planted beds along a side yard",
     "Camino de pasos de concreto entre jardineras a lo largo de un patio lateral"),
    (LI + "IMG_3067.jpeg", "walls",
     "Stepping-stone path set in gravel leading to a wood gate",
     "Camino de pasos sobre grava que lleva a un portón de madera"),
    (LI + "IMG_3072 (1).jpeg", "walls",
     "Wide concrete steps leading to a modern home entry with low planting",
     "Amplios escalones de concreto hacia la entrada de una casa moderna con plantación baja"),
    (LI + "IMG_3075.jpeg", "walls",
     "Flagstone walkway lined with flowering perennials",
     "Sendero de piedra laja bordeado de plantas perennes en flor"),
    (LI + "IMG_3086.PNG", "walls",
     "Flagstone stepping path through a gravel and mulch front yard",
     "Sendero de piedra laja por un jardín delantero de grava y mantillo"),
    (LI + "IMG_3073.jpeg", "walls",
     "Large concrete pads with gravel joints beside a turf lawn",
     "Grandes losas de concreto con juntas de grava junto a un césped"),

    # ---- Planting & Turf
    ("images/luna-sons-planting-bed-01.jpg", "planting",
     "Front-yard gravel bed with shrubs and perennials along a curved lawn edge",
     "Cama de grava en el jardín delantero con arbustos y perennes junto a un borde curvo de césped"),
    ("images/luna-sons-planting-bed-03.jpg", "planting",
     "Front-entry planting bed with foundation shrubs along a curved lawn edge",
     "Jardinera de entrada con arbustos de cimentación junto a un borde curvo de césped"),
    ("images/luna-sons-planting-bed-02.jpg", "planting",
     "Flowering shrub bed edged along a lawn in front of a home",
     "Jardinera de arbustos en flor junto a un césped frente a una casa"),
    ("images/luna-sons-retaining-wall-05.jpg", "planting",
     "Gravel planting corner with shrubs beside a sidewalk and wood fence",
     "Rincón de grava con arbustos junto a una banqueta y una cerca de madera"),
    ("images/luna-sons-backyard-turf-01.jpg", "planting",
     "Backyard turf lawn with steel edging, a gravel border and a pergola seating area",
     "Césped en el patio trasero con borde de acero, franja de grava y una zona de asientos bajo una pérgola"),
    ("images/luna-sons-front-yard-turf-01.jpg", "planting",
     "Front-yard turf lawn with a mulch border",
     "Césped en el jardín delantero con borde de mantillo"),
    (LI + "IMG_3036.JPG", "planting",
     "Lavender and ornamental planting beside a lawn and patio chairs in front of a stone-accented home",
     "Lavanda y plantas ornamentales junto a un césped y sillas de patio frente a una casa con detalles de piedra"),
    (LI + "IMG_3038.jpeg", "planting",
     "Rock-ringed bed with a ceramic fountain urn and ornamental grasses",
     "Cama rodeada de rocas con una urna-fuente de cerámica y pastos ornamentales"),
    (LI + "IMG_3048.jpeg", "planting",
     "River-rock bed with shrubs and perennials along a walkway",
     "Cama de piedra de río con arbustos y perennes a lo largo de un sendero"),
    (LI + "IMG_3050.jpeg", "planting",
     "Curved turf lawn beside a concrete patio in a backyard",
     "Césped curvo junto a un patio de concreto en un patio trasero"),
    (LI + "IMG_3053.jpeg", "planting",
     "Backyard turf lawn with stepping stones and planted beds",
     "Césped en el patio trasero con pasos de piedra y jardineras"),
    (LI + "IMG_3054.jpeg", "planting",
     "Turf side yard with concrete edging and a wood fence",
     "Patio lateral con césped, borde de concreto y cerca de madera"),
    (LI + "IMG_3055.jpeg", "planting",
     "Front-yard planting with a tree, a block planter and a curved turf edge",
     "Plantación en el jardín delantero con un árbol, una jardinera de bloque y un borde curvo de césped"),
    (LI + "IMG_3058.jpeg", "planting",
     "Ornamental grasses in a front-yard bed with a brick-colored border",
     "Pastos ornamentales en una jardinera delantera con borde color ladrillo"),
    (LI + "IMG_3059.jpeg", "planting",
     "Dry creek bed of river rock running through a front-yard planting bed",
     "Arroyo seco de piedra de río a través de una jardinera en el jardín delantero"),
    (LI + "IMG_3060.jpeg", "planting",
     "Front-yard gravel garden with a concrete walkway",
     "Jardín de grava en el frente de la casa con un sendero de concreto"),
    (LI + "IMG_3061.jpeg", "planting",
     "Front-yard turf lawn with a planted island beside a driveway",
     "Césped en el jardín delantero con una isla plantada junto a la entrada de autos"),
    (LI + "IMG_3062.jpeg", "planting",
     "Backyard lawn with seating, mulch beds and palm trees near a pool",
     "Césped en el patio trasero con asientos, camas de mantillo y palmeras junto a una alberca"),
    (LI + "IMG_3063.jpeg", "planting",
     "Modern front-yard gravel bed with a linear planter",
     "Cama de grava moderna en el jardín delantero con una jardinera lineal"),
    (LI + "IMG_3064.jpeg", "planting",
     "Curved-edged planting bed of river rock around a palm trunk",
     "Jardinera de borde curvo con piedra de río alrededor del tronco de una palmera"),
    (LI + "IMG_3065.jpeg", "planting",
     "Rock water feature with cascading stones and lush planting",
     "Elemento de agua con rocas en cascada y vegetación abundante"),
    (LI + "IMG_3066.jpeg", "planting",
     "Front-yard turf with a curved edge and river-rock border",
     "Césped en el jardín delantero con borde curvo y franja de piedra de río"),
    (LI + "IMG_3069.jpeg", "planting",
     "Drought-tolerant front-yard bed with boulders and gravel",
     "Cama resistente a la sequía en el jardín delantero con rocas grandes y grava"),
    (LI + "IMG_3070.jpeg", "planting",
     "Front-yard turf lawn with a curved gravel border and a boulder",
     "Césped en el jardín delantero con borde curvo de grava y una roca grande"),
    (LI + "IMG_3071.jpeg", "planting",
     "Turf backyard lawn running alongside a covered patio",
     "Césped en el patio trasero a lo largo de un patio techado"),
    (LI + "IMG_3074.jpeg", "planting",
     "Ornamental grasses and perennials in a bed beside a cobblestone paver edge",
     "Pastos ornamentales y perennes en una jardinera junto a un borde de adoquín"),
    (LI + "IMG_3076.jpeg", "planting",
     "Stepping stones through black mulch and turf in a front yard",
     "Pasos de piedra entre mantillo negro y césped en un jardín delantero"),
    (LI + "IMG_3083.PNG", "planting",
     "Gravel garden with ornamental grasses and shrubs in a front yard",
     "Jardín de grava con pastos ornamentales y arbustos en el frente de una casa"),
    (LI + "IMG_3084.PNG", "planting",
     "Turf front yard behind a white picket fence",
     "Césped en el jardín delantero detrás de una cerca blanca"),
    (LI + "IMG_3085.PNG", "planting",
     "Backyard putting green wrapping around a tree",
     "Green de práctica de golf en un patio trasero que rodea un árbol"),
    (LI + "IMG_3087.jpeg", "planting",
     "Front-yard bed of succulents, grasses and river rock",
     "Jardinera delantera con suculentas, pastos y piedra de río"),
    (LI + "IMG_3088.PNG", "planting",
     "Backyard turf lawn with a curved concrete edge and mulch beds",
     "Césped en el patio trasero con borde curvo de concreto y camas de mantillo"),
    (LI + "IMG_3089.PNG", "planting",
     "Lavender and flowering perennials among rocks and mulch",
     "Lavanda y plantas perennes en flor entre rocas y mantillo"),
    (LI + "IMG_3090.PNG", "planting",
     "Potted succulents and blue-gray grasses in a gravel bed",
     "Suculentas en maceta y pastos azul grisáceo en una cama de grava"),
    (LI + "IMG_3091.PNG", "planting",
     "Flowering plant with pink blooms in a gravel bed",
     "Planta con flores rosas en una cama de grava"),
]

# Six projects shown on the homepage (paths from _WORK above), in display order.
FEATURED = [
    NG + "IMG_3708.JPEG",
    NG + "IMG_3706.JPEG",
    "images/luna-sons-paver-patio-02.jpg",
    NG + "IMG_3709.jpeg",
    "images/luna-sons-planting-bed-01.jpg",
    "images/luna-sons-retaining-wall-03.jpg",
]


def _dims(path):
    # Read-only: the file itself is never modified.
    from PIL import Image
    with Image.open(os.path.join(SITE_ROOT, path)) as im:
        return im.size


# (path, width, height, category, alt_en, alt_es)
WORK = [(p, *_dims(p), c, en, es) for p, c, en, es in _WORK]
