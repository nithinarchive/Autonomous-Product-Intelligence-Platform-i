from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def process_events():
    print("Processing product events into warehouse")

with DAG(
    dag_id="product_event_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False
):
    PythonOperator(
        task_id="process_events",
        python_callable=process_events
    )
