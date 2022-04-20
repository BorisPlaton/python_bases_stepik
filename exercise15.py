with open('dataset_24465_4.txt') as o, open('new', "w") as n:
    lines = [i.strip() for i in o.readlines()]
    n.write('\n'.join(lines[::-1]))