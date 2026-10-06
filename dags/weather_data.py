from airflow import DAG 
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from data.extract import fetch_weather_data 
from data.transform import transform_weather_data 
from data.db_main import send_to_database


def extract_data():
    print("Extracting data...") 

def transform_data():
    print("Transforming data...")   

def load_data():
    print("Loading data...")



default_args = {
    "owner": "rmmuthoni", 
    "retries": 2, 
    "retry_delay": timedelta(minutes=1),
} 


with DAG(
    dag_id="weather_data_pipeline", 
    default_args=default_args, 
    description="Extracts data from Weather API, transforms, and sends to Warehouse", 
    schedule=timedelta(minutes=5),
    start_date=datetime(2026, 1, 1),
    catchup=False, 
    tags=["weather_data", "etl", "weather"],
) as dag: 

    extraction_task = PythonOperator(
        task_id="fetch_weather_data_from_api", 
        python_callable=fetch_weather_data,
    )

    transformation_task = PythonOperator(
        task_id="transform_data_from_crm", 
        python_callable=transform_data,
    ) 

    loading_task = PythonOperator(
        task_id="load_data_into_the_edw", 
        python_callable=load_data,
    )

    # Execution ORder 
    extraction_task >> transformation_task >> loading_task


