FROM python:3.11-slim

ARG BUILD_MODE=github  # default is github unless overridden
RUN useradd --system --shell /usr/sbin/nologin --home /app --no-create-home j2live
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN if [ "$BUILD_MODE" = "github" ]; then \
        git clone https://github.com/martydingo/j2live.git /app && \
        chown -R j2live:j2live /app ; \
    fi

COPY . /tmp_src
RUN if [ "$BUILD_MODE" = "local" ]; then \
        cp -r /tmp_src/* /app && \
        chown -R j2live:j2live /app ; \
    fi

USER j2live

RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install .

CMD ["/app/.venv/bin/python3", "-m", "j2live"]
