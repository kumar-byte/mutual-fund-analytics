import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*50)
print("UNIQUE FUND HOUSES")
print("="*50)
print(df["fund_house"].unique())

print("\n")
print("="*50)
print("UNIQUE CATEGORIES")
print("="*50)
print(df["category"].unique())

print("\n")
print("="*50)
print("UNIQUE SUB CATEGORIES")
print("="*50)
print(df["sub_category"].unique())

print("\n")
print("="*50)
print("UNIQUE RISK GRADES")
print("="*50)
print(df["risk_category"].unique())