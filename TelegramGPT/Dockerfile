FROM python:3.11.2-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_DEFAULT_TIMEOUT=30
ENV PIP_ROOT_USER_ACTION=ignore

# COPY src/ /opt/app/
# COPY statics/ /opt/statics
# COPY requirements.txt /opt/app/requirements.txt

# RUN pip3 install -r /opt/app/requirements.txt

WORKDIR /opt/app/
