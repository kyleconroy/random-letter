from lxml import etree

root = etree.parse("scripts/alpha.svg").getroot()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

header = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"id="Layer_1" viewBox="0 0 96 100" xml:space="preserve">
"""

footer = "</svg>"

for i, g in enumerate(root.findall(".//{http://www.w3.org/2000/svg}g")):
    with open("src/{}.svg".format(alpha[i]), "w") as f:
        f.write(header)
        f.write(etree.tostring(g, xml_declaration=False))
        f.write(footer)


