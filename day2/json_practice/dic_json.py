import json
data = {
    "name": "Yamada",
    "age": 30,
    "skills": ["Python", "JavaScript"]
}

# 辞書型をjson文字列に変換する
json_string = json.dumps(data)
print(json_string.__class__)
print(data.__class__)
