import streamlit as st
import pandas as pd

st.title("Banking Transactions Dashboard")

transactions = pd.read_csv("data/processed_transactions.csv")
frauds = pd.read_csv("data/fraud_alerts.csv")

st.header("Transaction Summary")
st.write(transactions.describe())

st.header("Fraudulent Transactions")
st.write(frauds)
