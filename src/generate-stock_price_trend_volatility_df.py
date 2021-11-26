# author : Group 30 - Block 3 - MDS UBC
# date : 2021-11-19

"""Collects a file containing the stocks price and trends weekly changes and percentages data to generates a .csv file containing the price and volume search volatilites for each stock.

Usage: generate-stock_price_trend_volatility_df.py --in_file=<in_file> --out_file=<out_file>

Options:
--in_file=<in_file>     Path (including filename) from where to retrieve the stocks weekly changes data (must be in standard csv format)
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
        "price_change_pct",
        "Sector",
        "pct_period_search_vol",
    }, "Required Columns not found in input .csv file"

    # Calculating the weekly price change as a percentage
    stock_trends_prices_stds = stock_price_trend_df.groupby(
        ["symbol", "Sector"], as_index=False
    ).agg({"price_change_pct": "std", "pct_period_search_vol": "std"})
    try:
        stock_trends_prices_stds.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        stock_trends_prices_stds.to_csv(out_file, index=False)


if __name__ == "__main__":
    main(opt["--in_file"], opt["--out_file"])
