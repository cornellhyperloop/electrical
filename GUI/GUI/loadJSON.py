import json

file = 'example2.json'
with open(file) as f:
        data = json.load(f)

print(data)