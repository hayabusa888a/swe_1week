#テスト用ファイル
import day4_pandas 
import pandas as pd


def test_filter_and_aggregate():
    df = pd.DataFrame({
    '顧客id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '支払金額': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    '日にち': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05'] })
    results = day4_pandas.filter_and_aggregate(df, '2023-01-01', 300)

    assert results == 0





