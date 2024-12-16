def detect_fraud(df):
    df["is_fraud"] = (df["amount"] > 10000) | (df.duplicated(subset=["account_id", "timestamp"], keep=False))
    return df[df["is_fraud"]]

if __name__ == "__main__":
    df = pd.read_csv("data/processed_transactions.csv")
    frauds = detect_fraud(df)
    frauds.to_csv("data/fraud_alerts.csv", index=False)
    print(f"Detected {len(frauds)} fraudulent transactions.")
