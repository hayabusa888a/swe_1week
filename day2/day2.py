import csv
import json
import argparse

#出力用の空のsetを作成
id_list = set()

parser = argparse.ArgumentParser()

parser.add_argument('--date')
parser.add_argument('--min_amount')

args = parser.parse_args()  

#csvを読み込む
with open('./day2_sample.csv') as f:
    reader = csv.DictReader(f) #1行目をヘッダーとして読み込む
    for row in reader: #1行ずつ抽出
	#日にち、金額が条件を満たす
        if row['日にち'] == args.date and int(row['支払金額']) >= int(args.min_amount):
            id_list.add(row['顧客id']) #顧客idを追加
data = { "人数": len(id_list)}
json_str = json.dumps(data, indent = 2, ensure_ascii = False) #json形式で保存

print(json_str)
            
            
    