from datetime import datetime, timedelta
# from airflow import models
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from openlineage.airflow import DAG

default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay": timedelta(seconds=30),
}

PROJECT_ID = "my-project-id"
DATASET_ID = "my_dataset"
TABLE_ID = "my_table" 

dag = DAG('lineage_test_dag', default_args=default_args, schedule_interval=None, start_date=datetime(2021, 1, 1), tags=["bigquery"])

run_this = BigQueryOperator(
    task_id="run_this",
    sql=f"CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}_2` (someName STRING, dateTime TIMESTAMP);",
    use_legacy_sql=False,
    dag=dag
)

run_this_after = BigQueryOperator(
    task_id="run_this_after",
    sql=f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}_2` LIMIT 1000",
    use_legacy_sql=False,
    dag=dag
)


run_this >> run_this_after

