FROM python:3.10

ARG PROJECT_ID
ARG ACCESS_TOKEN

# RUN ls $ACCESS_TOKEN

# ENV PYTHONFAULTHANDLER=1 \
#   PYTHONUNBUFFERED=1 \
#   URL=https://token:${ACCESS_TOKEN}@git.id-network.ru/api/v4/projects/${PROJECT_ID}/packages/pypi/simple \
#   POETRY_VERSION=1.1.5

# # RUN pip install "poetry==$POETRY_VERSION"
# RUN ls $ACCESS_TOKEN
RUN pip install fm-http-client --index-url https://token:${ACCESS_TOKEN}@git.id-network.ru/api/v4/projects/${PROJECT_ID}/packages/pypi/simple

