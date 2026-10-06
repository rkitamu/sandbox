# sandbox

技術検証用の Python スクリプト置き場。1検証 = `scripts/` 配下の1ファイル。

## 必要なもの

- [uv](https://docs.astral.sh/uv/)（Python 3.14 は uv が用意する）
- Docker（コンテナで実行する場合のみ）
- AWS を叩くスクリプトは `AWS_REGION` と認証情報（`AWS_PROFILE` またはアクセスキー）

## 実行

```sh
# ローカル
uv run --locked scripts/<スクリプト>.py [引数...]

# Docker（スクリプトはイメージにコピーされるので、編集後は --build が必要）
docker compose run --rm --build app scripts/<スクリプト>.py [引数...]
```

Docker 実行時は、ホストの AWS 関連の環境変数と `~/.aws`（読み取り専用）がコンテナに渡される。

## スクリプト

| ファイル | 内容 |
| --- | --- |
| `scripts/bedrock_similarity.py` | Bedrock InvokeModel（Titan Text Embeddings V2）で2つのテキストを埋め込み、cosine similarity を出す |

```sh
uv run --locked scripts/bedrock_similarity.py "犬が好き" "猫が好き"
```

## 検証を追加する

1. `scripts/` にファイルを置く
2. 依存が必要なら `uv add <パッケージ>`（`pyproject.toml` と `uv.lock` が更新されるので両方コミットする）
3. 上の表に1行足す
