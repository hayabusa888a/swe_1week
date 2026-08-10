import json
data = data = {
    "name": "Yamada",
    "age": 30,
    "skills": ["Python", "JavaScript"]
}

# 辞書型をjson文字列に変換してjson ファイルに書き込む
with open('data.json', 'w') as file:
    json.dump(data, file)
