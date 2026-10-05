from airflow import DAG 
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta


def extract_data():
    print("Extracting data...") 

def transform_data():
    print("Transforming data...")   

def load_data():
    print("Loading data...")



default_args = {
    "owner": "rmmuthoni@outlook.com", 
    "retries": 2, 
    "retry_delay": timedelta(minutes=1),
} 


with DAG(
    dag_id="etl_for_customer_crm_data_source_sap", 
    default_args=default_args, 
    description="This DAG is used to extract, transform, and loand data from the customer SAP CRM data source and loads it into the data worehouse for further analysis.", 
    schedule=timedelta(minutes=1),
    start_date=datetime(2026, 1, 1),
    catchup=False, 
    tags=["etl", "customer_crm_data_source_sap"],
) as dag: 

    extraction_task = PythonOperator(
        task_id="extract_data_from_crm", 
        python_callable=extract_data,
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


