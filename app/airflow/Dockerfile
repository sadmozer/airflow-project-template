FROM apache/airflow:2.3.0-python3.8

USER root
RUN apt-get update \
  && apt-get install -y \
        python3-dev build-essential libmysqlclient-dev\
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /tmp/requirements.txt

# TODO: Fix Bigquery local server configuration
# ENV BIGQUERY_EMULATOR_HOST http://localhost:9050

RUN pip install -r /tmp/requirements.txt --no-cache-dir