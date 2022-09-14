## 開発環境構築

```shell
# docker-compose.ymlのあるディレクトリでDocker Imageのビルド
docker-compose build
# コンテナ&サーバー起動
docker-compose up
```

## DBの初期化
Docker内で以下のコマンドを叩く。

```shell
# DBの最新化と初期データ投入
alembic upgrade head
python load_data.py
```

## DBの初期化
```shell
# スクリプトの起動
python answer.py
```
## 文法チェックとテスト

```shell
# コーディング規約のチェック
$ flake8 app
# 型チェック
$ mypy app
# コードフォーマットの修正
$ black app
# 全部チェック
$ black app && flake8 app && mypy app
```
