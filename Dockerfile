FROM python:3.10-slim-bullseye

RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        vim \
        netcat \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .