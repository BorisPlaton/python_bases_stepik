from xml.etree import ElementTree


d = {}


def get_children(root, level):
    d[root.attrib['color']] = d[root.attrib['color']] + level if d.get(root.attrib['color']) else level
    for child in root:
        get_children(child, level + 1)


tree = ElementTree.fromstring(input())
get_children(tree, 1)
print(f"{d['red']} {d['green']} {d['blue']}")
