FROM apache/airflow:1.10.15-python3.8

USER root
RUN curl -s http://repo.mysql.com/RPM-GPG-KEY-mysql-2022 | apt-key add -
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

RUN pip install -r /tmp/requirements.txt --no-cache-dir --use-feature=2020-resolver