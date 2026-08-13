## Day1 学習内容

### git基礎
[サル先生のGit入門](https://git-tutorial.backlog.com/) を用いて、Gitの基礎を学習した。

### Python基礎
Claudeとの対話を通して、immutable（不変）とmutable（可変）の違いを学習。
実際にコードを書いて理解を深めた。

## Day2 学習内容

### 簡単なCLIツールの作成
CSVファイルを読み込み、特定の条件で集計し、結果を出力するスクリプトを作成した。

### 学んだこと

**csvモジュールでのCSVファイルの扱い方**
```python
with open('パス') as f:
    reader = csv.DictReader(f)
```

**JSON形式（テキスト形式）へのエンコード方法**（`data` は辞書）
```python
json_str = json.dumps(data, indent=2, ensure_ascii=False)  # JSON形式で保存
```

**argparseモジュールについて**
コマンドライン上で引数を受け取りたいときに便利

## Day4学習内容

### コードリーディング
デコレーターについて。関数やクラスの前後に特定の処理を追加することのできるもの。
```python
@retry(max_attempts=3, delay=1)
def fetch_data(url):
#これは fetch_data = retry(max_attempts=3, delay=1)(fetch_data)と同義になる。
```

### オブジェクト指向
クラス（設計図）を用いてインスタンス（もの）を生成する。クラスは、属性（インスタンスごとのデータ）とメソッド（関数）をからなる。

## Day4学習内容

### pandas基礎
pandasを利用することで、データinput(read_csv)から条件分岐、json変換(to_json)まで簡単にできる

### pytest
テスト用のスクリプトを作成して、関数のテストを実行。期待出力は自分で定義する必要あり。
元の関数をimportするのだが、元関数のスクリプトで以下を書かないとエラーになる。（main関数には、元関数のスクリプトを直接実行したときに動作してほしい処理を書く。）
```python
if __name__ == "__main__":
    main()
```
if __name__ == "__main__":　これは言い換えると、元関数のファイルがモジュールとして別のファイルで読み込まれたときに、以下の処理を実行しないようにするif文と捉えることができる。

## Day5学習内容

### SQL応用
window関数を用いた集計方法を学習。かならず連番を振りたい時は、row_number()、同じ値の時は同じ順位にしたい時はrank()を用いる。
row_number()の注意点として、同じ値の時に、order byに追加でそれらの順序を一意に決定するカラムを追加しないと、実行結果が不確実になってしまう。（実行環境やタイミングで結果が変わる可能性あり）
　
