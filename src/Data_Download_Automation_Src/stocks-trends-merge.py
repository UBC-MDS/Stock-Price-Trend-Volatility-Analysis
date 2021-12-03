import os
import pandas as pd

all_stocks_trend_data = pd.DataFrame()
stocks_file_names = os.listdir("./google-trends-data")

for file in stocks_file_names:
    if not file.startswith("."):
        trends_data = pd.read_csv(
            f"./google-trends-data/{file}", skiprows=3, header=None
        )
        trends_data["symbol"] = file[0:-4]
        trends_data.columns = ["week", "weekly_interest", "symbol"]
        all_stocks_trend_data = all_stocks_trend_data.append(
            trends_data, ignore_index=True
        )

all_stocks_trend_data.to_csv("./stock_trend_data.csv")