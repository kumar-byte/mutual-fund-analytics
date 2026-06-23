import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf")

print("Database created successfully!")