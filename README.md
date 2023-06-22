# python-base

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

***

## Setup

### ホスト環境

- Docker（v2以降。Docker、Docker-compose利用可能の環境。なお、v1はDepricated。）
- VSCode

### 事前準備

- `.ssh/`配下のサンプルに従い、GitHub Enterprise用のsshキーの作成
- `.env.sample`に従い`.env`ファイルを作成
- `/backend/.env.sample`に従い`/backend/.env`ファイルを作成

### コンテナビルド

- dockerコマンドで実行

    初回時もしくはDockerfile書き換え時などビルドが必要なとき

    ```sh
    # $ cd <プロジェクトルートフォルダ>
    $ docker compose -f compose.development.yaml up -d --build
    ```

    ビルド不要のとき

    ```sh
    # $ cd <プロジェクトルートフォルダ>
    $ docker compose -f compose.development.yaml up -d
    ```

- makeコマンドで実行

    事前準備

    ```sh
    # ホスト環境にmakeをインストール
    # (e.g.) ubuntuの場合 (gccとmakeのインストール)
    $ sudo apt install build-essential
    ```

    初回時もしくはDockerfile書き換え時などビルドが必要なとき

    ```sh
    # $ cd <プロジェクトルートフォルダ>
    $ make docker_compose_development_build_and_up
    ```

    ビルド不要な時

    ```sh
    # $ cd <プロジェクトルートフォルダ>
    $ make docker_compose_development_up
    ```

### Dev Containerの使用 (backendのコンテナ使用例)

- ホスト上のVSCodeで`/workspace/backend`のフォルダを開く
- コマンドの`Dev Container: Rebuild Without Cahce and Open in Container`を選択

***

## Git, GitHub

### commit comment

commit時のコメントは[Commitizen](https://commitizen-tools.github.io/commitizen/)を参考に、Prefixを付けます。

  ```sh
  fix: バグの修正
  feat: 機能追加
  docs: ドキュメントのみの変更
  style: コードの動作に影響しない、見た目だけの変更 (スペース、フォーマット、欠落の修正、セミコロンなど)
  refactor: バグの修正や機能の追加ではないコードの変更
  perf: パフォーマンスを向上させるコードの変更
  test: 不足しているテストの追加や、既存のテストの修正
  build: ビルドシステムや外部依存関係に影響を与える変更 (example scopes: pip, docker, npm)
  ci: CI設定ファイルおよびスクリプトの変更 (example scopes: GitLabCI, TravisCI)
  ```

### pre-commit

commit時、pre-commitにより`.pre-commit-config.yaml`に指定の処理が走る。  
どれかでエラーが発生した場合はコミットが成功しないため、ファイルを修正する。
