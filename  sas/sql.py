import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:    @localhost:5432/nasser")

df = pd.read_csv("/Users/zakaria/Desktop/ sas/health_data_cleaned.csv")

print(df.head(10))