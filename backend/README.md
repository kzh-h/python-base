# backend

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

***

## コンテナ内セットアップ

### 前提

- .gitが作成されていること

### コマンド

```sh
# コンテナ内のCLI
$ make container_init
```

### Interpreterの設定

`settings.json`に記載の`python.defaultInterpreterPath`は環境によって違う名前が付けられる場合があるため、
コンテナ内で以下のコマンドでディレクトリ名を確認し修正する。  
また、初期立ち上げ時はVSCode右下のInterpreterも該当する仮想環境を選択する。

```sh
ls /opt/pysetup/.venv
```

***

## パッケージ追加・削除

パッケージのインストール

```sh
$ poetry add <module> 
# 開発環境のみ
$ poetry add <module> --group dev
```

***

## スクリプト実行

```sh
cd /workspace/backend/src
poetry run python hello_world.py
# すでに仮想環境に入っている場合はpoetry run不要
```

```sh
# 仮想環境に入る。すでに仮想環境に入っている場合は不要。
$ poetry shell
(python3-11-base-py3.11) $ cd /workspace/backend/src
(python3-11-base-py3.11) $ cd python hello_world.py
# 仮想環境から出る
(python3-11-base-py3.11) $ exit
```

***

## テスト、静的解析

テストについて、特に指定がない場合、`/workspace/backend/tests`配下の`test_*.py`の`test_*`のメソッドをすべて実行

### すべて一括実行

```sh
poetry run nox 
```

もしくは

```sh
# 仮想環境に入る
$ poetry shell
(python3-11-base-py3.11) $ nox
# 仮想環境から出る
(python3-11-base-py3.11) $ exit
```

### テストのみ実行

```sh
# $ cd /workspace/backend
$ pytest
```

もしくは

```sh
# 仮想環境に入る
$ poetry shell
(python3-11-base-py3.11) $ pytest
# 仮想環境から出る
(python3-11-base-py3.11) $ exit
```
