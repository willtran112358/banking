# Banking Transaction Data Pipeline for Fraud Detection - PoC for VPBank

This **Proof of Concept (PoC)** demonstrates a banking transaction data pipeline for **fraud detection** at VPBank. It includes components for **data ingestion**, **ETL processing**, **fraud detection**, and **visualization** to support real-time transaction monitoring.

### **Key Features**:
- **Synthetic Data Generation**: Simulates banking transactions for testing.
- **ETL Pipeline**: Automates data extraction, transformation, and loading using Python, Apache Spark, and Airflow.
- **Fraud Detection**: Detects suspicious activities (e.g., large transactions, rapid consecutive transactions).
- **Data Visualization**: Provides a dashboard to monitor trends and fraud alerts using Streamlit.

This PoC is scalable for integration into VPBank’s infrastructure to enhance fraud detection and transaction monitoring.

### **Tech Stack**:
- **Languages**: Python 3.x
- **Libraries**: 
  - **Pandas**, **PySpark** for data processing
  - **Apache Airflow** for ETL orchestration
  - **Faker** for synthetic data
  - **Streamlit** for interactive dashboards
  - **PostgreSQL** for data storage


## Project Structure

```plaintext
banking-data-pipeline/
├── README.md                      # Project documentation
├── data/
│   ├── transactions.csv            # Sample transaction data (synthetic)
├── src/
│   ├── data_generator.py           # Script for generating synthetic transaction data
│   ├── etl_pipeline.py             # ETL pipeline script (data cleaning and transformation)
│   ├── fraud_detection.py          # Fraud detection logic
│   ├── data_visualization.py       # Streamlit app for dashboard visualization
├── dags/
│   ├── etl_dag.py                  # Airflow DAG for scheduling the ETL tasks
├── db/
│   ├── init.sql                    # Database schema for transactions
├── requirements.txt                # Python dependencies
└── docker-compose.yml              # Docker setup for running services
