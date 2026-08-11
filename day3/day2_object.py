#day2で作成した集計コードをオブジェクト指向コードに書き換える
#クラス：salesAggregator
#属性：csvパス、集計日、最小金額
#メソッド：csv読み込み、フィルター・集計、json変換・出力


import csv
import json
import argparse


class SalesAggregator:
    def __init__(self, csv_path, date, min_amount):
        self.csv_path = csv_path
        self.date = date
        self.min_amount = int(min_amount)
    
    def load_csv(self):
        with open(self.csv_path) as f:
            reader = csv.DictReader(f)
            return list(reader)

    def filter_and_aggregate(self, rows):
        customer_ids = set()
        for row in rows:
            if row['日にち'] == self.date and int(row['支払金額']) >= self.min_amount:
                    customer_ids.add(row['顧客id']) #顧客idを追加 
        return customer_ids         

    def to_json(self, customer_ids):
        data = { "人数": len(customer_ids)}  
        return json.dumps(data, indent = 2, ensure_ascii = False) #json形式で保存
  
    def run(self):
        rows = self.load_csv()
        customer_ids = self.filter_and_aggregate(rows)
        return self.to_json(customer_ids)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date')
    parser.add_argument('--min_amount')
    args = parser.parse_args()  
    sales = SalesAggregator('../day2/day2_sample.csv', args.date, args.min_amount) 
    print(sales.run())

if __name__ == "__main__":
    main()