ARG IMAGE_NAME

# python-base
FROM ${IMAGE_NAME} as python-base

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.4.1 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    # POETRY_VIRTUALENVS_PATHに仮想環境を作るため、コメントアウト。
    # IN_PROJECTにすると、docker composeのマウント対象でローカルのもので上書きされてしまうため。
    # POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/workspace/backend" \
    POETRY_VIRTUALENVS_PATH="/opt/pysetup/.venv" 

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin::$PATH"


# build
FROM python-base as builder-base

# APTの最新化及びシステムコマンドのインストール
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends \
    # deps for installing poetry
    curl \
    # deps for building python deps
    build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml README.md ./
COPY ./src/ ./src/

# install runtime deps
RUN poetry install --no-dev


# development
FROM python-base as development

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"

WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
    git \
    sudo \
    task-japanese \
    locales-all \
    tree \
    make \
    openssh-client

ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

# quicker install as runtime deps are already installed
RUN poetry install