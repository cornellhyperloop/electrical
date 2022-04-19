import json

file = 'ex.json'
with open(file) as f:
    data = json.load(f)

print(data)
