FROM python:3.9-slim
WORKDIR /src
RUN apt-get -y update && \
  apt-get install -y python3-dev default-libmysqlclient-dev build-essential && \
  apt-get install -y curl apt-transport-https && \
  apt-get autoremove -y && \
  apt-get clean
ENV LANG en_US.utf8
RUN apt-get -y update
COPY pyproject.toml poetry.lock /src/
RUN pip install -U pip && \
  pip install --no-cache-dir poetry && \
  poetry config virtualenvs.create false && \
  poetry install && \
  rm pyproject.toml poetry.lock
