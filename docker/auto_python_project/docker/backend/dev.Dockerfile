FROM python:3.11-buster AS builder

RUN apt-get update && apt-get install -y --no-install-recommends python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install poetry

FROM builder AS builder-venv

COPY pyproject.toml /pyproject.toml
RUN /venv/bin/poetry install --no-root

FROM builder-venv AS tester

COPY ./src /src
WORKDIR /src
RUN /venv/bin/poetry run pytest tests

