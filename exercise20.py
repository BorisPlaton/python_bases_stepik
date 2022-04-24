import re

import requests


def find_link(link_start, link_end):
    links = find_all_links(requests.get(link_start).text)
    if link_end in links:
        return True


def find_all_links(text):
    pattern = r'<a href="(.+)">'
    links = re.findall(pattern, text)
    return links


link_a = input()
link_b = input()
f = False

first_links = find_all_links(requests.get(link_a).text)
for link in first_links:
    if find_link(link, link_b):
        f = True
        break

print("Yes") if f else print("No")
