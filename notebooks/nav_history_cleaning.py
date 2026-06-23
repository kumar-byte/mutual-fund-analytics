import pandas as pd

# Load file
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 50)
print("ORIGINAL DATA")
print("=" * 50)

print(df.head())
print(df.shape)

# -------------------------
# Convert date column
# -------------------------
df["date"] = pd.to_datetime(df["date"])

# -------------------------
# Sort values
# -------------------------
df = df.sort_values(
    by=["amfi_code", "date"]
)

# -------------------------
# Missing values
# -------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------
# Forward fill NAV
# -------------------------
df["nav"] = df["nav"].ffill()

# -------------------------
# Remove duplicates
# -------------------------
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicates Removed:", before - after)

# -------------------------
# NAV Validation
# -------------------------
invalid_nav = df[df["nav"] <= 0]

print("\nInvalid NAV Records:")
print(len(invalid_nav))

# Keep only valid NAV
df = df[df["nav"] > 0]

# -------------------------
# Save cleaned file
# -------------------------
df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

print("\nClean file saved!")
print(df.shape)