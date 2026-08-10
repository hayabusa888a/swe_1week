# json文字列を辞書型に変換する
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)

print(data["name"])  # Output: John
print(data["age"])   # Output: 30