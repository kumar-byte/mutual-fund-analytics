import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_nav.csv")

fund_codes = set(fund["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = nav_codes - fund_codes

print("Missing codes:", missing)
print("Count:", len(missing))