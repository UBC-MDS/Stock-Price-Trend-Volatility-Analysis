import pandas as pd

stock_trend_path = "./stock_trend_data.csv"
stock_price_path = "./stock_price_data.csv"

trends_df = pd.read_csv(stock_trend_path, index_col=0)
prices_df = pd.read_csv(stock_price_path, index_col=0)

prices_trends_merged_df = trends_df.merge(prices_df, on=["symbol", "week"])
prices_trends_merged_df.to_csv("prices_trends_merged_data.csv")
