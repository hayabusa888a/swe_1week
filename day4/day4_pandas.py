#day2で作成しtあfilter_and_aggregate関数をpandasで書き換える
import pandas as pd
import argparse


df = pd.read_csv('../day2/day2_sample.csv', encoding = 'shift_jis')

def filter_and_aggregate(df, date, min_amount):
    df = df[(df['支払金額'] >= int(min_amount)) & (df['日にち'] == date)]
    customer_ids = df['顧客id'].nunique()
    return customer_ids

parser = argparse.ArgumentParser()
parser.add_argument('--date')
parser.add_argument('--min_amount')
args = parser.parse_args()  
date = args.date
min_amount = args.min_amount

if __name__ == "__main__":
    main()

def main():
    print(filter_and_aggregate(df, date, min_amount))



