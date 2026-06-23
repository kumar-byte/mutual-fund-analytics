import pandas as pd
#amfi_validation
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("="*50)
print("AMFI CODE VALIDATION")
print("="*50)

print(f"Fund Master Codes : {len(fund_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\n All AMFI codes exist in NAV History")
else:
    print(f"\n Missing Codes Count: {len(missing_codes)}")
    print(missing_codes)