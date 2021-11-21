import os
import pandas as pd
from datetime import timedelta

all_stocks_price_data = pd.DataFrame()
stocks_file_names = os.listdir("./yahoo-finance-data")

for file in stocks_file_names:
    if not file.startswith("."):
        price_data = pd.read_csv(f"./yahoo-finance-data/{file}")
        price_data["symbol"] = file[0:-4]
        price_data = price_data[["Date", "Open", "Adj Close", "symbol"]]

        # Match week open to google trends week open
        price_data["Date"] = pd.to_datetime(price_data["Date"]) - timedelta(days=1)

        price_data.columns = ["week", "open", "adj_close", "symbol"]
        all_stocks_price_data = all_stocks_price_data.append(
            price_data, ignore_index=True
        )

all_stocks_price_data.to_csv("./stock_price_data.csv")
