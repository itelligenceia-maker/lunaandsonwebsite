"""
New / replaced service pages for the outdoor-living-first redesign, plus hero photos for
every service page. Same data shape as PAGES in build_service_pages.py.
Strings use '&amp;' where the original builder does (they are written into HTML as-is).
"""

CTA_BTN = ("Schedule a Consultation", "Programar una Consulta")


def im(src, w, h, alt_en, alt_es):
    return {"src": src, "width": w, "height": h, "alt": (alt_en, alt_es)}


HERO = {
    "outdoor-living-patios": im("luna-sons-pergola-01.jpg", 1600, 1120,
        "Hardtop pergola over a paver patio with a stone-clad seating area and gravel bed",
        "Pérgola con techo sobre un patio de adoquines, con área de asientos revestida de piedra y jardín de grava"),
    "landscape-design": im("luna-sons-planting-bed-03.jpg", 1600, 1120,
        "Front-entry planting bed with hostas, coral bells, and ornamental grasses",
        "Jardín de entrada con hostas, campanillas de coral y pastos ornamentales"),
    "landscape-construction": im("luna-sons-retaining-wall-01.jpg", 1600, 1292,
        "Curved segmental block planters framing a brick-home entry",
        "Jardineras curvas de bloque enmarcando la entrada de una casa de ladrillo"),
    "pavers-retaining-walls": im("luna-sons-retaining-wall-04.jpg", 1600, 1120,
        "Home with a curved walkway and finished planting beds",
        "Casa con un sendero curvo y jardineras terminadas"),
    "planting-irrigation": im("luna-sons-planting-bed-01.jpg", 1600, 1292,
        "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
        "Jardín de rocas resistente a la sequía con algodoncillo en flor y pastos ornamentales junto a un borde curvo de césped"),
    "landscape-maintenance": im("luna-sons-front-yard-turf-01.jpg", 971, 1600,
        "Completed front yard with turf and landscaping",
        "Jardín delantero terminado con césped y paisajismo"),
}

EXTRA_PAGES = [
    {
        "slug": "outdoor-living-patios",
        "meta_title": "Outdoor Living &amp; Patios | Luna &amp; Sons Landscaping",
        "meta_description": "Custom patios, pergolas and outdoor living spaces in Santa Maria and the Central Coast — thoughtfully designed and carefully built by Luna &amp; Sons Landscaping.",
        "title": ("Outdoor Living &amp; Patios", "Vida al Aire Libre y Patios"),
        "subheading": (
            "Patios, pergolas and gathering spaces designed around the way you live.",
            "Patios, pérgolas y espacios para reunirse, diseñados según su forma de vivir.",
        ),
        "hero_image_note": "outdoor living hero",
        "intro_paragraphs": [
            (
                "Your yard should feel like an extension of your home. We design and build outdoor living spaces — patios, seating and dining areas, pergolas, planters and the planting that surrounds them — around how you actually entertain, relax and spend time outside.",
                "Su jardín debe sentirse como una extensión de su hogar. Diseñamos y construimos espacios de vida al aire libre — patios, áreas de estar y comedor, pérgolas, jardineras y la plantación que los rodea — según cómo usted realmente recibe, descansa y disfruta el exterior.",
            ),
        ],
        "intro_image_note": "paver patio",
        "intro_image": im("luna-sons-paver-patio-02.jpg", 1123, 1600,
            "Paver patio with a lounge sofa and dining set beneath a brick chimney backdrop",
            "Patio de adoquines con sofá lounge y juego de comedor frente a una chimenea de ladrillo"),
        "blocks": [
            {
                "heading": ("Designed Around How You Live", "Diseñado Según Su Forma de Vivir"),
                "body": [(
                    "Every outdoor living project starts with a conversation: how many people you host, where the sun and shade fall, and how the space connects to your home. We use that to shape a layout that feels natural from the first day.",
                    "Todo proyecto de vida al aire libre comienza con una conversación: a cuántas personas recibe, dónde caen el sol y la sombra, y cómo se conecta el espacio con su casa. Con eso damos forma a un diseño que se siente natural desde el primer día.",
                )],
                "image_side": "right", "image_note": "patio layout",
                "image": im("luna-sons-flagstone-patio-02.jpg", 1600, 1120,
                    "Irregular flagstone patio with a yellow bistro set beside a moss-covered boulder accent",
                    "Patio de piedra laja irregular con un juego de bistró amarillo junto a una roca decorativa cubierta de musgo"),
            },
            {
                "heading": ("Materials That Hold Up", "Materiales Que Perduran"),
                "body": [(
                    "Pavers, flagstone and natural stone are chosen for how they look and how they perform over time on the Central Coast. Careful base preparation and clean detailing are what keep a patio level and beautiful for years.",
                    "Los adoquines, la piedra laja y la piedra natural se eligen por su apariencia y por su desempeño a largo plazo en la Costa Central. Una base bien preparada y acabados limpios son lo que mantiene un patio nivelado y hermoso por años.",
                )],
                "image_side": "left", "image_note": "pergola",
                "image": im("luna-sons-pergola-01.jpg", 1600, 1120,
                    "Hardtop pergola over a paver patio with a stone-clad seating area and gravel bed",
                    "Pérgola con techo sobre un patio de adoquines, con área de asientos revestida de piedra y jardín de grava"),
            },
            {
                "heading": ("A Complete Transformation", "Una Transformación Completa"),
                "body": [(
                    "A patio is often just the start. We can bring walls, planting, lighting and irrigation into the same plan so the whole yard feels finished and cohesive.",
                    "Un patio suele ser solo el comienzo. Podemos integrar muros, plantación, iluminación y riego en un mismo plan para que todo el jardín se sienta terminado y coherente.",
                )],
                "image_side": "right", "image_note": "flagstone patio",
                "image": im("luna-sons-flagstone-patio-01.jpg", 1600, 1292,
                    "Flagstone patio with a natural stone accent feature in a completed Luna & Sons backyard",
                    "Patio de piedra laja con un elemento decorativo de piedra natural en un patio terminado por Luna & Sons"),
            },
        ],
        "cta_heading": ("Ready to create your outdoor space?", "¿Listo para crear su espacio exterior?"),
        "cta_button_text": CTA_BTN,
    },
    {
        "slug": "pavers-retaining-walls",
        "meta_title": "Pavers &amp; Retaining Walls | Luna &amp; Sons Landscaping",
        "meta_description": "Paver patios, walkways and retaining walls in Santa Maria and the Central Coast — built with careful base preparation and drainage by Luna &amp; Sons Landscaping.",
        "title": ("Pavers &amp; Retaining Walls", "Adoquines y Muros de Contención"),
        "subheading": (
            "Clean lines and lasting strength — pavers, walkways and walls built to last.",
            "Líneas limpias y gran resistencia — adoquines, senderos y muros construidos para durar.",
        ),
        "hero_image_note": "pavers and walls hero",
        "intro_paragraphs": [
            (
                "Hardscape is the framework of a landscape. We build paver patios, walkways, steps and retaining walls with careful grading, drainage and base preparation, so the finished result stays level, stable and good-looking.",
                "El hardscape es la estructura de un paisaje. Construimos patios de adoquines, senderos, escalones y muros de contención con nivelación, drenaje y preparación de base cuidadosos, para que el resultado se mantenga nivelado, estable y atractivo.",
            ),
        ],
        "intro_image_note": "paver walkway",
        "intro_image": im("luna-sons-paver-walkway-01.jpg", 971, 1600,
            "Square concrete paver walkway set in pea gravel along a side-yard privacy fence",
            "Camino de adoquines de concreto cuadrados sobre grava junto a una cerca lateral privada"),
        "blocks": [
            {
                "heading": ("Pavers &amp; Walkways", "Adoquines y Senderos"),
                "body": [(
                    "From entry paths to side-yard walkways and patio surfaces, pavers give a clean, durable finish in a range of colors, textures and patterns.",
                    "Desde senderos de entrada hasta caminos laterales y superficies de patio, los adoquines ofrecen un acabado limpio y duradero en una variedad de colores, texturas y patrones.",
                )],
                "image_side": "right", "image_note": "paver patio",
                "image": im("luna-sons-paver-patio-02.jpg", 1123, 1600,
                    "Paver patio with a lounge sofa and dining set beneath a brick chimney backdrop",
                    "Patio de adoquines con sofá lounge y juego de comedor frente a una chimenea de ladrillo"),
            },
            {
                "heading": ("Retaining Walls &amp; Planters", "Muros de Contención y Jardineras"),
                "body": [(
                    "Retaining walls manage slopes and create usable level space, while curved planters and seat walls add shape and definition to a yard. We plan each one with drainage and structure in mind.",
                    "Los muros de contención controlan las pendientes y crean espacio plano utilizable, mientras que las jardineras curvas y los muros para sentarse aportan forma y definición al jardín. Planificamos cada uno pensando en el drenaje y la estructura.",
                )],
                "image_side": "left", "image_note": "retaining wall",
                "image": im("luna-sons-retaining-wall-01.jpg", 1600, 1292,
                    "Curved segmental block planters framing a brick-home entry",
                    "Jardineras curvas de bloque enmarcando la entrada de una casa de ladrillo"),
            },
            {
                "heading": ("Built for the Long Term", "Construido a Largo Plazo"),
                "body": [(
                    "The part of a hardscape project you can't see — excavation, compacted base and drainage — is what determines how it holds up. That's where we put our care.",
                    "La parte de un proyecto de hardscape que no se ve — excavación, base compactada y drenaje — es la que determina cuánto dura. Ahí es donde ponemos nuestro cuidado.",
                )],
                "image_side": "right", "image_note": "curved wall",
                "image": im("luna-sons-retaining-wall-03.jpg", 1123, 1600,
                    "Curved stone retaining wall planter with purple-flowering shrubs above an artificial turf lawn",
                    "Jardinera curva de muro de piedra con arbustos de flores púrpuras sobre un césped artificial"),
            },
        ],
        "cta_heading": ("Ready to build something lasting?", "¿Listo para construir algo duradero?"),
        "cta_button_text": CTA_BTN,
    },
    {
        "slug": "planting-irrigation",
        "meta_title": "Planting &amp; Irrigation | Luna &amp; Sons Landscaping",
        "meta_description": "Water-wise planting and efficient irrigation in Santa Maria and the Central Coast — designed, installed and repaired by Luna &amp; Sons Landscaping.",
        "title": ("Planting &amp; Irrigation", "Plantación y Riego"),
        "subheading": (
            "Water-wise planting and efficient irrigation that thrive on the Central Coast.",
            "Plantación eficiente en agua y riego eficaz que prosperan en la Costa Central.",
        ),
        "hero_image_note": "planting hero",
        "intro_paragraphs": [
            (
                "Planting is what makes a landscape feel alive, and irrigation is what keeps it that way. We design planting around your site, exposure and water use, and install efficient irrigation so your landscape stays healthy without waste.",
                "La plantación es lo que da vida a un paisaje, y el riego es lo que lo mantiene así. Diseñamos la plantación según su sitio, su exposición y su consumo de agua, e instalamos riego eficiente para que su paisaje se mantenga sano sin desperdicio.",
            ),
        ],
        "intro_image_note": "planting bed",
        "intro_image": im("luna-sons-planting-bed-03.jpg", 1600, 1120,
            "Front-entry planting bed with hostas, coral bells, and ornamental grasses",
            "Jardín de entrada con hostas, campanillas de coral y pastos ornamentales"),
        "blocks": [
            {
                "heading": ("Planting Designed for Your Site", "Plantación Diseñada Para Su Sitio"),
                "body": [(
                    "We choose plants for their color, texture and form as well as how they perform in Central Coast conditions, then group them by water need so the landscape looks good through the seasons.",
                    "Elegimos las plantas por su color, textura y forma, así como por su desempeño en las condiciones de la Costa Central, y las agrupamos según su necesidad de agua para que el paisaje luzca bien en todas las estaciones.",
                )],
                "image_side": "right", "image_note": "drought-tolerant planting",
                "image": im("luna-sons-planting-bed-01.jpg", 1600, 1292,
                    "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
                    "Jardín de rocas resistente a la sequía con algodoncillo en flor y pastos ornamentales junto a un borde curvo de césped"),
            },
            {
                "heading": ("Efficient Irrigation", "Riego Eficiente"),
                "body": [(
                    "Drip and sprinkler systems are zoned to match the plants they serve. We install new systems and repair or upgrade existing ones to improve coverage and reduce wasted water.",
                    "Los sistemas de goteo y aspersión se dividen en zonas según las plantas que atienden. Instalamos sistemas nuevos y reparamos o mejoramos los existentes para mejorar la cobertura y reducir el desperdicio de agua.",
                )],
                "image_side": "left", "image_note": "planting bed",
                "image": im("luna-sons-planting-bed-02.jpg", 1600, 1292,
                    "Finished planting bed by Luna & Sons",
                    "Jardinera terminada por Luna & Sons"),
            },
        ],
        "cta_heading": ("Ready to plan your planting?", "¿Listo para planificar su plantación?"),
        "cta_button_text": CTA_BTN,
    },
    {
        "slug": "landscape-maintenance",
        "meta_title": "Landscape Maintenance | Luna &amp; Sons Landscaping",
        "meta_description": "Ongoing landscape maintenance in Santa Maria, CA — mowing, seasonal planting refreshes, irrigation checks, fertilization, and year-round upkeep.",
        "title": ("Landscape Maintenance", "Mantenimiento de Paisaje"),
        "subheading": (
            "Ongoing care to keep your landscape looking its best, year-round.",
            "Cuidado continuo para que su paisaje luzca lo mejor posible durante todo el año.",
        ),
        "hero_image_note": "maintenance hero",
        "intro_paragraphs": [
            (
                "A landscape is an investment — regular maintenance is what protects it.",
                "Un paisaje es una inversión — el mantenimiento regular es lo que la protege.",
            ),
        ],
        "intro_image_note": "maintained landscape",
        "intro_image": im("luna-sons-planting-bed-01.jpg", 1600, 1292,
            "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
            "Jardín de rocas resistente a la sequía con algodoncillo en flor y pastos ornamentales junto a un borde curvo de césped"),
        "blocks": [
            {
                "heading": ("Ongoing Care", "Cuidado Continuo"),
                "body": [(
                    "Our maintenance services include routine mowing and trimming, seasonal planting refreshes, irrigation checks and repairs, fertilization, and general upkeep tailored to your property's needs.",
                    "Nuestros servicios de mantenimiento incluyen corte y poda de rutina, renovación estacional de plantas, revisión y reparación de riego, fertilización y mantenimiento general adaptado a las necesidades de su propiedad.",
                )],
                "image_side": "right", "image_note": "maintained landscape",
                "image": im("luna-sons-retaining-wall-03.jpg", 1123, 1600,
                    "Curved stone retaining wall planter with purple-flowering shrubs above an artificial turf lawn",
                    "Jardinera curva de muro de piedra con arbustos de flores púrpuras sobre un césped artificial"),
            },
            {
                "heading": ("One-Time or Ongoing", "Única Vez o Continuo"),
                "body": [(
                    "Whether you need a one-time cleanup or a standing maintenance schedule, our team treats every property like it's our own. We've built our reputation on doing the small things right, consistently.",
                    "Ya sea que necesite una limpieza única o un programa de mantenimiento continuo, nuestro equipo trata cada propiedad como si fuera propia. Hemos construido nuestra reputación haciendo bien las pequeñas cosas, de manera constante.",
                )],
                "image_side": None,
            },
        ],
        "cta_heading": ("Ready for ongoing care?", "¿Listo para el cuidado continuo?"),
        "cta_button_text": CTA_BTN,
    },
]
