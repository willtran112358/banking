from faker import Faker
import random
import csv
from datetime import datetime, timedelta

fake = Faker()
transaction_types = ["deposit", "withdrawal", "transfer"]
statuses = ["completed", "pending", "failed"]

def generate_transaction():
    return {
        "transaction_id": fake.uuid4(),
        "account_id": fake.uuid4(),
        "timestamp": fake.date_time_between(start_date="-1y", end_date="now"),
        "amount": round(random.uniform(10.0, 10000.0), 2),
        "transaction_type": random.choice(transaction_types),
        "location": fake.city(),
        "status": random.choice(statuses),
    }

def write_transactions_to_csv(file_path, num_records):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(generate_transaction().keys()))
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow(generate_transaction())

if __name__ == "__main__":
    write_transactions_to_csv("data/transactions.csv", 10000)
