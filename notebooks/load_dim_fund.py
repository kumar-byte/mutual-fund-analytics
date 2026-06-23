import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost/bluestock_mf"
)

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

print(fund_df.head())
print(fund_df.shape)

fund_df.to_sql(
    "dim_fund",
    con=engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded successfully!")