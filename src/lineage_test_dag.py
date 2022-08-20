from datetime import datetime, timedelta
from airflow import models
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay": timedelta(seconds=30),
}

PROJECT_ID = "my-project-id"
DATASET_ID = "my-dataset"
TABLE_ID = "my-table" 

with models.DAG(
    dag_id="lineage_test_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["bigquery"],
    default_args=default_args
) as dag:
    run_this = BigQueryExecuteQueryOperator(
        task_id="run_this",
        sql=f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` LIMIT 1000",
        location="europe-west6",
        use_legacy_sql=False
    )
    run_this