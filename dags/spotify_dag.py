from datetime import timedelta
from airflow import dag
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from spotify_etl import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False
    'start_date' : days_ago(2022, 8, 17, 14, 00, 00), #year,month,day,hour,minutes,seconds
    'email' : ['arunpannala12@gmail.com']
    'email_on_failure' : False,
	'email_on_retry' : False, 
	'retries' : 1,
	'retry_delay' : timedelta(minutes = 1)
}

dag = DAG(
    'spotify_dag'
    default_args=default_args,
    description='Spotify ETl'
    schedule_interval=timedelta(days=1),
)

def spotify_etl():
    print("Spotify etl function")

run_spotify_etl = PythonOperator(
	task_id="complete_etl",
	python_callable=spotify_etl,
	dag=dag
)

run_spotify_etl