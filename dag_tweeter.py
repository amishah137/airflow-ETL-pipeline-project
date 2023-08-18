from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from etl_tweeter import run_etl

default_args = {
    'owner': 'Ami_Shah',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 17),
    'email': ['amishah137@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    dag_id='dag_tweeter',
    default_args=default_args,
    description='Our DAG with Tweeter ETL process!',
    schedule_interval=timedelta(days=1),
    )

run_etl = PythonOperator(
    task_id='complete_etl_tweeter',
    python_callable=run_etl,
    dag=dag, 
)

run_etl

