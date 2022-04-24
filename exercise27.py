import re
import requests

pattern = r"""<a(?:.*|\s)href=(?:'|")(?:\w+:\/\/)?([a-zA-z0-9\-]+\.[a-zA-Z.0-9\-]+)[\/]?"""
links = set(re.findall(pattern, requests.get(input()).text))
links = list(links)
links.sort()
print(*links, sep='\n')