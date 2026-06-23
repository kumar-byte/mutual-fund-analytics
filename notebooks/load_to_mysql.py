from sqlalchemy import create_engine
import pandas as pd

# --------------------------
# MySQL Connection
# --------------------------

engine = create_engine(
    "mysql+pymysql://root:root@localhost/bluestock_mf"
)

# --------------------------
# FACT NAV
# --------------------------

nav_df = pd.read_csv("data/processed/clean_nav.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"]).dt.date

nav_df.to_sql(
    "fact_nav",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded successfully!")

# --------------------------
# FACT TRANSACTIONS
# --------------------------

trans_df = pd.read_csv("data/processed/clean_transactions.csv")

trans_df["transaction_date"] = pd.to_datetime(
    trans_df["transaction_date"]
).dt.date

trans_df.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded successfully!")

# --------------------------
# FACT PERFORMANCE
# --------------------------

perf_df = pd.read_csv("data/processed/clean_performance.csv")

perf_df.to_sql(
    "fact_performance",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded successfully!")

# --------------------------
# FACT AUM
# --------------------------

aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum_df["date"] = pd.to_datetime(aum_df["date"]).dt.date

aum_df = aum_df[
    [
        "fund_house",
        "aum_crore",
        "date",
        "aum_lakh_crore",
        "num_schemes"
    ]
]

aum_df.to_sql(
    "fact_aum",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_aum loaded successfully!")

print("\nAll data loaded successfully!")