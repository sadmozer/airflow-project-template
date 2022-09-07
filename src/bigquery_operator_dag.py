"""
Example Airflow DAG for Google BigQuery service testing dataset operations.
"""
from datetime import datetime

from airflow import models
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator
)

PROJECT_ID = "my-project-id"
DATASET_ID = f"my_dataset"

with models.DAG(
    dag_id="bigquery_operator_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["bigquery"],
) as dag:

    create_dataset = BigQueryCreateEmptyDatasetOperator(task_id="create_dataset", project_id=PROJECT_ID, dataset_id=DATASET_ID)
    
    create_dataset