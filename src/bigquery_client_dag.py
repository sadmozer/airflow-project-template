"""
Example Airflow DAG for Google BigQuery service testing dataset operations.
"""
import os
from datetime import datetime

from airflow import models
from airflow.operators.python import PythonOperator

PROJECT_ID = "my-project-id"
DATASET_ID = f"my_dataset"

def query_fun():
    from google.cloud import bigquery

    client = bigquery.Client()

    query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
    """
    query_job = client.query(query)

    print("The query data:")
    for row in query_job:
        print("name={}, count={}".format(row[0], row["total_people"]))

with models.DAG(
    dag_id="bigquery_client_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["bigquery"],
) as dag:

    run_query = PythonOperator(task_id="query", python_callable=query_fun)
    
    run_query