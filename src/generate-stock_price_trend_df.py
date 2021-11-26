# author : Group 30 - Block 3 - MDS UBC
# date : 2021-11-19

"""Collects a file containing the stocks price and trends weekly data and generates a combined .csv file along with their weekly change percentages

Usage: generate-stock_price_trend_df.py --in_file=<in_file> --out_file=<out_file>

Options:
--in_file=<in_file>     Path (including filename) from where to retrieve the stocks weekly data (must be in standard csv format)
--out_file=<out_file>   Path (including filename) of where to locally write the file
"""

import pandas as pd
import os
from docopt import docopt

opt = docopt(__doc__)


def main(in_file, out_file):
    # Check if input and output files are .csv files
    assert in_file.endswith(
        ".csv"
    ), "Input file is not a .csv file, please enter a .csv file as the <in_file>"

    assert out_file.endswith(
        ".csv"
    ), "Output file is not a .csv file, please enter a .csv file as the <out_file>"

    stock_price_trend_df = pd.read_csv(in_file)

    # Check if input columns match the required columns
    assert set(stock_price_trend_df.columns) == {
        "symbol",
        "adj_close",
        "open",
        "week",
        "weekly_interest",
        "Sector",
    }, "Required Columns not found in input .csv file"

    # Calculating the weekly price change as a percentage
    stock_price_trend_df["price_change_pct"] = (
        stock_price_trend_df["adj_close"] - stock_price_trend_df["open"]
    ) / stock_price_trend_df["open"]
    # Calculating the Google Trends weekly_interest as a percentage of the yearly search volume
    stock_price_trend_df["pct_period_search_vol"] = (
        stock_price_trend_df["weekly_interest"]
        / stock_price_trend_df.groupby("symbol")["weekly_interest"].transform("sum")
    ) * 100
    try:
        stock_price_trend_df.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        stock_price_trend_df.to_csv(out_file, index=False)


if __name__ == "__main__":
    main(opt["--in_file"], opt["--out_file"])
