from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from datetime import datetime
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl

#Define a DAG 
dafault_args={
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2020 , 11 , 8),
    'email' : ['airflow@emaple.com'],
    'email_on_failture' : False,
    'emai_on_retry' : False,
    'retries': 1,
    'retries_delay' : timedelta(minutes=1)
    }

dag = DAG(
    'twitter_dag',
    default_args= dafault_args,
    description = 'my first etl code'
    )

#create a PythonOperator
run_etl = PythonOperator(
    task_id = 'complete_twitter_etl',
    #python callable : its which python function you want to call
    pyhton_callable=run_twitter_etl,
    dag=dag
    )
