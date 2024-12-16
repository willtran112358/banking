import pandas as pd

def process_transaction_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df[df["status"] == "completed"]  # Keep only completed transactions
    df["amount_usd"] = df["amount"].apply(lambda x: round(x * 0.85, 2))  # Currency conversion
    df.to_csv(output_path, index=False)
    print("ETL process completed successfully.")

if __name__ == "__main__":
    process_transaction_data("data/transactions.csv", "data/processed_transactions.csv")
  
