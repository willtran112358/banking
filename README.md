# Banking Transaction Data Pipeline for Fraud Detection

This project demonstrates a scalable data engineering pipeline for processing and analyzing financial transaction data in the banking and finance domain. It includes components for data ingestion, transformation, fraud detection, and visualization, aiming to provide insights into suspicious activity.

## Project Overview

The solution processes simulated banking transactions to detect potentially fraudulent activities using a rule-based detection system. It also generates reports and visualizations to support decision-making in the banking sector.

### Key Features

- **Data Simulation**: Generate synthetic transactional data with Faker.
- **ETL Pipeline**: Process and clean data using Apache Spark/Pandas.
- **Fraud Detection**: Implement rule-based fraud detection (e.g., large transactions, rapid consecutive transactions).
- **Data Storage**: Store processed data in a PostgreSQL database.
- **Visualization**: Create interactive dashboards using Streamlit for fraud detection insights.

## Tech Stack

- **Programming Languages**: Python
- **Libraries**:
  - **Faker**: For generating synthetic transaction data.
  - **Pandas**: For data transformation and cleaning.
  - **PySpark**: For distributed data processing (optional).
  - **PostgreSQL**: For storing transaction data.
  - **Streamlit**: For creating interactive dashboards.
- **Other Tools**:
  - **Apache Airflow** (or **Prefect**) for orchestration of the ETL pipeline.
  - **Docker**: For containerizing the application.

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
