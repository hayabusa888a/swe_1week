import json

with open('data.json', 'r') as file:
    data = json.load(file)
print(data["name"])  # Output: John