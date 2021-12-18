from datetime import timedelta, datetime
# The DAG object; we'll need this to instantiate a DAG

# Operators; we need this to operate!
from airflow.operators.python_operator import PythonOperator
from airflow import DAG
from api_to_redis import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'sqlite_dag',
    default_args = default_args,
    description='first sqlite dag',
    schedule_interval=timedelta(minutes=1),
    start_date=datetime(2021, 12, 9)
)

run_etl = PythonOperator(
    task_id='etl_sqlite',
    python_callable=main,
    dag=dag
)
