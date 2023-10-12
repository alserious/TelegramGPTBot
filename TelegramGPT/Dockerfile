FROM python:3.11.2-slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive

ARG IS_PROD

RUN apt-get update

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_DEFAULT_TIMEOUT=60
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /opt/app/

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /opt/app/

RUN poetry config virtualenvs.create false \
    && poetry install $(test "$IS_PROD" == prod && echo "--no-dev") --no-interaction --no-ansi

COPY telegramgpt/ /opt/app/
