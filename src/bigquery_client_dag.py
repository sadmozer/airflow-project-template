"""
Example Airflow DAG for Google BigQuery service testing dataset operations.
"""
import os
from datetime import datetime

from airflow import models
from airflow.operators.python_operator import PythonOperator

PROJECT_ID = "my-project-id"
DATASET_ID = "my_dataset"
TABLE_ID = "my_table" 

def query_fun():
    from google.cloud import bigquery

    client = bigquery.Client()

    query = f"""
        SELECT *
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        LIMIT 1000
    """
    query_job = client.query(query)

with models.DAG(
    dag_id="bigquery_client_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["airflow_1"],
) as dag:

    run_query = PythonOperator(task_id="query", python_callable=query_fun)
    
    run_query