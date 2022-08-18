FROM apache/airflow:2.2.5-python3.8
USER airflow
COPY requirements.txt /tmp/requirements.txt

# TODO: Fix Bigquery local server configuration
# ENV BIGQUERY_EMULATOR_HOST http://localhost:9050

RUN pip install -r /tmp/requirements.txt --no-cache-dirs