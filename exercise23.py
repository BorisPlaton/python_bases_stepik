import json


def count_parents(node):

    if not node['parents']:
        return

    for parent in node['parents']:
        print(node)
        if not node['name'] in nodes[parent]['children']:
            nodes[parent]['child'] += 1
            nodes[parent]['children'].add(node['name'])
        count_parents(nodes[parent])


nodes = {}
visited_nodes = set()
file = json.loads(input())

for record in file:
    nodes[record['name']] = {'name': record['name']}
    nodes[record['name']]['parents'] = record['parents']
    nodes[record['name']]['child'] = 1
    nodes[record['name']]['children'] = set()

for record in nodes.values():
    if record['name'] not in visited_nodes:
        count_parents(record)
        visited_nodes.add(record['name'])

items = list(nodes.items())
items.sort()

for i in items:
    print(f"{i[0]} : {i[1]['child']}")
