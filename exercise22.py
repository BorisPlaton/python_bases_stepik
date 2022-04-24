import csv
from collections import Counter

with open('Crimes.csv') as f:
    reader = csv.DictReader(f)
    types = Counter()
    for row in reader:
        types.update([row['Primary Type']])

print(types.most_common(n=True))

