  ## 課題
- 本リポジトリをcloneして開発を行う。
- question.mdにある内容について回答コードを作成する。
- 回答コードは、分かりやすい名前を付けたブランチをpushすることで提出とする。
- 以下の通り開発環境構築を行い、サンプルコードの実行などを確認すること。

## 開発環境構築

無料のVS Code または 有料版のIntelliJを用いて、docker, python関連の開発環境を整える。

参考 [VS Code, Docker, Pythonの開発環境構築方法](https://chigusa-web.com/blog/vs-code%E3%81%A7docker%E3%81%AEpython%E7%92%B0%E5%A2%83%E3%81%A7%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E9%96%8B%E7%99%BA/)

次に、本リポジトリのカレントディレクトリにて以下のコマンドを実行し、dockerを立ち上げる。

```shell
# docker-compose.ymlのあるディレクトリでDocker Imageのビルド
docker-compose build
# コンテナ&サーバー起動
docker-compose up
```

## DBの初期化
まずDocker内に接続する。

Docker desktopアプリからUI上で接続するか、docker execコマンドを用いる。

Docker内で以下のコマンドを叩く。

```shell
# DBの最新化と初期データ投入
alembic upgrade head
python load_data.py
```

## スクリプトの起動
Docker内で以下のコマンドを叩く。
```shell
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
