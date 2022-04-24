import requests


facts = {

}
with open('dataset_24476_3.txt') as f:
    nums = [i.rstrip() for i in f.readlines()]
print(nums)

for num in nums:
    response = requests.get(f'http://numbersapi.com/{num}/math?json=true').json()
    facts[num] = 'Interesting' if response['found'] else 'Boring'

print(*facts.values(), sep='\n')
