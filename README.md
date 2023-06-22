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

### branch model

`GitHub Flow`をベースとした branch model を採用します。

```sh
少人数での開発にしては堅苦しすぎるかもしれませんが、以下の理由からbranch modelを決めた方がよいと考えます。
・大規模開発を踏まえたgitの勉強になる
・コンフリクトやバグの発見を早期に行えるため、手戻りが少なくなる
```

1. **ブランチは master と feature の 2 種類だけを使用する**  
  feature ブランチは最新の master ブランチから作成します。
  feature ブランチは機能ごとに作成するようにしてください。
  （ex. 入力フォームを作ろう！ ⇒ `feature/forms`ブランチを作成する）  
  また、master ブランチは直接編集してはいけません。必ず feature ブランチを master ブランチから作成し、feature ブランチ上で編集を行ってください。  
  |#|種類|編集可否|作成元|マージ先|
  |---|---|---|---|---|
  |1|master|×|-|-|
  |2|feature|〇|master|master|

2. **master は常にリリース可能な状態にする**  
  アジャイル開発において、リリースは特別なイベントであってはいけません。リリースの負荷を軽減するため常に動く ≒ リリース可能な状態を保つ必要があります。  
  そのため、後述する 3~5 のルールを守って master は常に動作する状態にします。

3. **master に merge する際は必ず Pull Request を出す**  
  feature ブランチでの開発が終わり、master に merge する際は必ず Pull Request を出します。Pull Request を出すことで 3 つの利点が得られます。

    - コードにレビューを行う（ルール 4）ため、レビュワー・レビューイともに成長できる
    - 複数人の目を通すことでバグを早期に発見することができる
    - 他者が書いたコードを目にする機会が増えるため、スキトラの手間が減る

4. **Pull request に対して必ずコードレビューを行う**
  コードレビューを通じてバグの早期発見・スキルの伝播が期待できます。レビュワーは自環境での動作確認 & コードの確認を行う必要があります。

5. **feature ブランチは細かく push & merge する**  
  1 Pull Request の修正量が多いとレビュワーの負荷が増加し、Pull Request の習慣が往々にして形骸化します。
  小さな修正を細かく反映することで Pull Request ループの成功体験が蓄積され気持ちよく開発できます。

  ```sh
  とは言え、高頻度のコードレビューによってレビューイの手が止まってしまうので短期的な作業効率は落ちると思います。
  （プロジェクト外活動でレビュワーがすぐに動けないことも多いと思うので、作業効率の低下はなおのこと）
  進めていきながら最適なバランスを見つけられればと思っています。
  ```

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

commitizenを使用することで、CLI上で対話的にcommit commentの作成も可能。

  ```sh
  # 変更をstaging
  $ git add .

  # 変更をcommit
  $ cz commit
  # 対話的にcommentを作成していく
  ? Select the type of change you are committing (Use arrow keys)
  » fix: A bug fix. Correlates with PATCH in SemVer
    feat: A new feature. Correlates with MINOR in SemVer
    docs: Documentation only changes
    style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    refactor: A code change that neither fixes a bug nor adds a feature
    perf: A code change that improves performance
    test: Adding missing or correcting existing tests
    build: Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)
    ci: Changes to our CI configuration files and scripts (example scopes: GitLabCI)
  ...

  # 変更をpush
  $ git push -u origin head
```

### pre-commit

commit時、pre-commitにより`.pre-commit-config.yaml`に指定の処理が走る。  
どれかでエラーが発生した場合はコミットが成功しないため、ファイルを修正する。
