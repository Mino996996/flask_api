# flask_api

## 仮想環境の手順

一度環境を作成すれば OK

windows 用（コマンドプロンプトで。bash は NG）

```
環境の作成
py -3 -m venv venv

環境の作成
venv\Scripts\activate

立ち上がった仮想環境でFlaskのインストール
pip install Flask

サーバー立ち上げ
flask --app hello run --host=0.0.0.0

```

以降はコマンドプロンプトから
venv\Scripts\activate
flask --app hello run --host=0.0.0.0

で OK。
