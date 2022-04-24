import requests
import json

client_id = '49424c2a9cba81e3c53a'
client_secret = 'dfc9a9481c5717ecae6ce4d795b6bf1b'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

token = r.json()["token"]
headers = {"X-Xapp-Token": token}
l = []
with open('dataset_24476_4.txt', encoding='utf-8') as f:
    for i in f.readlines():
        r = requests.get(f"https://api.artsy.net/api/artists/{i.rstrip()}", headers=headers)
        r.encoding = 'utf-8'
        l.append((r.json()['sortable_name'], r.json()['birthday']))

l.sort(key=lambda x: (x[1], x[0]))
for name in l:
    print(name[0])
