from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

# Set up Python environment path to include the src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import the Python scripts for ETL tasks
from data_generator import write_transactions_to_csv
from etl_pipeline import process_transaction_data
from fraud_detection import detect_fraud

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'banking_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for banking transaction data and fraud detection',
    schedule_interval=timedelta(days=1),  # Runs daily
    catchup=False,  # Do not run for past dates
) as dag:

    # Task 1: Generate synthetic data
    generate_data_task = PythonOperator(
        task_id='generate_transaction_data',
        python_callable=write_transactions_to_csv,
        op_args=['data/transactions.csv', 10000],  # Generate 10,000 transactions
        dag=dag,
    )

    # Task 2: Run ETL pipeline (clean and transform data)
    etl_task = PythonOperator(
        task_id='process_transaction_data',
        python_callable=process_transaction_data,
        op_args=['data/transactions.csv', 'data/processed_transactions.csv'],
        dag=dag,
    )

    # Task 3: Run fraud detection
    fraud_detection_task = PythonOperator(
        task_id='fraud_detection',
        python_callable=detect_fraud,
        op_args=['data/processed_transactions.csv'],
        dag=dag,
    )

    # Define task dependencies
    generate_data_task >> etl_task >> fraud_detection_task
