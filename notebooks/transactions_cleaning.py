import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print(df.isnull().sum())

print(df.duplicated().sum())

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

df = df[df["amount_inr"] > 0]
# print(df.columns.tolist())

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print(df["kyc_status"].value_counts())

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)