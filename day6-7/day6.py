import pandas as pd
import sqlite3

class Transaction_Aggregate:
    def __init__(self, customer_path, product_path, transaction_path, db_path):
        self.customer_path = customer_path
        self.product_path = product_path
        self.transaction_path = transaction_path
        self.db_path = db_path

    def load_data(self):
        df_customer = pd.read_csv(self.customer_path)
        df_product = pd.read_csv(self.product_path)
        df_transaction = pd.read_csv(self.transaction_path)
        return df_customer, df_product, df_transaction

    def aggregate_by_age(self, df_customer, df_product, df_transaction):
        df_customer['age_bin'] = (df_customer['年齢']//10)*10
        df_t_c = pd.merge(df_transaction, df_customer, on='顧客id', how='left')
        df_t_c = df_t_c.groupby('取引id').agg({'合計金額': 'sum', 'age_bin': 'first'}).reset_index()
        df_t_c = df_t_c.groupby('age_bin')['合計金額'].mean().reset_index()
        return df_t_c

    def aggregate_by_category(self, df_customer, df_product, df_transaction):
        df_t_p = pd.merge(df_transaction, df_product, on='商品id', how='left')
        df_t_p = df_t_p.groupby(['取引id', 'カテゴリ'])['個数'].sum().reset_index()
        df_t_p = df_t_p.groupby('カテゴリ')['個数'].mean().reset_index()
        return df_t_p

    def save_to_db(self, summary1, summary2):
        conn = sqlite3.connect(self.db_path)
        summary1.to_sql('age_summary', conn, if_exists='replace', index=False)
        summary2.to_sql('category_summary', conn, if_exists='replace', index=False)
        conn.close()
    
    
    def run(self):
        df_customer, df_product, df_transaction = self.load_data()
        summary1 = self.aggregate_by_age(df_customer, df_product, df_transaction)
        summary2 = self.aggregate_by_category(df_customer, df_product, df_transaction)
        self.save_to_db(summary1, summary2)
        return summary1, summary2
def main ():
    sales = Transaciton_Aggregate('./sample_data/customers.csv', './sample_data/products.csv', './sample_data/transactions.csv', './output/output.db')
    summary1, summary2 = sales.run()
    print(summary1)
    print(summary2)

if __name__ == '__main__':
    main()