import re
import requests

pattern = r'<a .+ href="(?:.+:\/\/)?((?:\w|\.)+).+">'
links = list(set(re.findall(pattern, requests.get(input()).text)))
links.sort()
print(links, sep='\n')
