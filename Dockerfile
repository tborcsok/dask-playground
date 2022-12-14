FROM python:3.10-slim as installer

RUN apt-get update
RUN apt-get install -y build-essential
RUN pip install -U pip wheel
RUN pip install poetry


WORKDIR /opt

RUN poetry config virtualenvs.in-project true --local
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root

# Final stage
FROM python:3.10-slim

COPY --from=installer /opt/.venv /opt/.venv
ENV PATH=/opt/.venv/bin:$PATH
