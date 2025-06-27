import simplequant as sq
import pandas as pd

df = pd.read_csv("data/sample_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

symbols = df['Symbol'].unique().tolist()
dates = df['Date'].unique().tolist()
alpha_df = sq.run_parallel_alpha(df, symbols=symbols, dates=dates, n_jobs=16)

print(alpha_df)