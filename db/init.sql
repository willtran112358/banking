CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY,
    account_id UUID,
    timestamp TIMESTAMP,
    amount DECIMAL(10, 2),
    transaction_type VARCHAR(20),
    location VARCHAR(100),
    status VARCHAR(20)
);
