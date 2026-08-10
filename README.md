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

