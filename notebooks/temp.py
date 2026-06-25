import pandas as pd

df = pd.read_csv("../data/raw/sbi_bluechip_nav.csv")

print(df.columns)
print(df.head())