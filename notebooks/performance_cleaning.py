import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.columns.tolist())

df["return_1yr_pct"] = pd.to_numeric(df["return_1yr_pct"])
df["return_3yr_pct"] = pd.to_numeric(df["return_3yr_pct"])
df["return_5yr_pct"] = pd.to_numeric(df["return_5yr_pct"])

# print(df[["return_1yr_pct",
#           "return_3yr_pct",
#           "return_5yr_pct"]].dtypes)

negative_sharpe = df[df["sharpe_ratio"] < 0]

print("Negative Sharpe Ratio Funds:")
print(negative_sharpe[["scheme_name","sharpe_ratio"]])

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(invalid_expense[
    ["scheme_name","expense_ratio_pct"]
])

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Performance data cleaned successfully!")