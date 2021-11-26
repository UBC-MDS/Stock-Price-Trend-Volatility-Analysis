# author : Group 30 - Block 3 - MDS UBC
# date : 2021-11-19

"""Collects a .csv file containing the stocks price and trends volatility data and generates a number of volatility plots.

Usage: generate-plot-images.py --in_file=<in_file> --out_folder=<out_folder>

Options:
--in_file=<in_file>         Path (including filename) from where to retrieve the stocks volatility data (must be in standard csv format)
--out_folder=<out_folder>   Folder path of where to save the plots as .png files
"""

import pandas as pd
import os
from docopt import docopt
import altair as alt

opt = docopt(__doc__)


def main(in_file, out_folder):
    # Check if input file is a .csv file
    assert in_file.endswith(
        ".csv"
    ), "Input file is not a .csv file, please enter a .csv file as the <in_file>"

    stock_trends_prices_stds_df = pd.read_csv(in_file)

    # Check if input columns match the required columns
    assert set(stock_trends_prices_stds_df.columns) == {
        "symbol",
        "price_change_pct",
        "Sector",
        "pct_period_search_vol",
    }, "Required Columns not found in input .csv file"

    # Plotting the standard deviations of the price change percentages for all stocks as a distribution
    plt_price_stds = (
        alt.Chart(
            stock_trends_prices_stds_df, title="Distribution of Price Change Volatility"
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "price_change_pct",
                bin=alt.Bin(maxbins=100),
                title="Stock Price Weekly Percentage Change (StDev)",
            ),
            y=alt.Y("count()", title="Count of Stocks"),
        )
    )

    # Plotting the standard deviations of the percentage of period search volumes on Google for all stocks as a distribution
    plt_trends_searchvols_stds = (
        alt.Chart(
            stock_trends_prices_stds_df,
            title="Distribution of Stock search volume Volatility",
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "pct_period_search_vol",
                bin=alt.Bin(maxbins=100),
                title="Weekly Google Search vol (StDev)",
            ),
            y=alt.Y("count()", title="Count of Stocks"),
        )
    )

    # Combining volatility distribution plots
    volatility_distribution_plots = plt_price_stds | plt_trends_searchvols_stds

    ## Creating sector volitility distribution plots

    # Plotting the standard deviations of the price change percentages for each business sector as a distribution
    plt_sectors_price_stds = (
        alt.Chart(
            stock_trends_prices_stds_df, title="Distribution of Price Change Volatility"
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "price_change_pct",
                bin=alt.Bin(maxbins=50),
                title="Stock Price Weekly Percentage Change (StDev)",
            ),
            y=alt.Y("count()", title="Count of Stocks"),
            color="Sector",
        )
        .properties(height=100)
        .facet(
            "Sector",
            columns=1,
            title="Distribution of Price Change Volatility Based on Business Sectors",
        )
    )

    # Plotting the standard deviations of the search volume percentage for each business sector as a distribution
    plt_sectors_trends_searchvol_stds = (
        alt.Chart(
            stock_trends_prices_stds_df,
            title="Distribution of Stock Search Volume Volatility",
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "pct_period_search_vol",
                bin=alt.Bin(maxbins=50),
                title="Search volume percentage (StDev)",
            ),
            y=alt.Y("count()", title="Count of Stocks"),
            color="Sector",
        )
        .properties(height=100)
        .facet(
            "Sector",
            columns=1,
            title="Distribution of Stock Search Volume Percentage Volatility Based on Business Sectors",
        )
    )

    sectors_volatility_distribution_plots = (
        plt_sectors_price_stds
        | plt_sectors_trends_searchvol_stds.properties(
            data=stock_trends_prices_stds_df.sample(
                stock_trends_prices_stds_df.shape[0]
            )
        )
    )

    plt_searchvols_prices_stds = (
        alt.Chart(stock_trends_prices_stds_df)
        .mark_point(opacity=0.4, color="gray")
        .encode(
            x=alt.X(
                "pct_period_search_vol",
                title="Search volume percentage volatility(StDev)",
            ),
            y=alt.Y("price_change_pct", title="Stock price volatility(StDev)"),
        )
    )

    # Plot the prices and search volume percentages regression
    stocks_prices_searchvols_reg = (
        plt_searchvols_prices_stds
        + plt_searchvols_prices_stds.transform_regression(
            "pct_period_search_vol", "price_change_pct"
        ).mark_line()
    )

    # Plotting the prices and search volume percentages regression per business sectors
    plt_sectors_searchvol_prices_stds = (
        alt.Chart(stock_trends_prices_stds_df)
        .mark_point(opacity=0.6, filled=True)
        .encode(
            x=alt.X(
                "pct_period_search_vol",
                title="Weekly Search Vol Change on Google(StDev)",
            ),
            y=alt.Y("price_change_pct", title="Stock Price Percentage Change(StDev)"),
            color="Sector",
        )
    )

    plt_searchvol_prices_stds_sector = (
        alt.Chart(stock_trends_prices_stds_df)
        .mark_point(opacity=0.6, filled=True)
        .encode(
            x=alt.X("pct_period_search_vol", title=""),
            y=alt.Y("price_change_pct", title=""),
            color=alt.Color("Sector", legend=None),
        )
    )

    plt_searchvol_prices_sector_faceted = (
        plt_searchvol_prices_stds_sector
        + plt_searchvol_prices_stds_sector.transform_regression(
            "pct_period_search_vol", "price_change_pct"
        )
        .properties(height=160, width=160)
        .mark_line()
    ).facet("Sector", columns=4)

    sectors_stocks_prices_searchvols_reg = alt.hconcat(
        plt_sectors_searchvol_prices_stds, plt_searchvol_prices_sector_faceted
    ).configure_legend(labelFontSize=0, symbolSize=0, title=None)

    # Creating the plot files
    try:
        volatility_distribution_plots.save(
            f"{out_folder}/volatility_distribution_plots.png", scale_factor=5.0
        )
        sectors_volatility_distribution_plots.save(
            f"{out_folder}/sectors_volatility_distribution_plots.png", scale_factor=5.0
        )

        stocks_prices_searchvols_reg.save(
            f"{out_folder}/stocks_prices_searchvols_reg.png", scale_factor=5.0
        )

        sectors_stocks_prices_searchvols_reg.save(
            f"{out_folder}/sectors_stocks_prices_searchvols_reg.png", scale_factor=5.0
        )
    except:
        os.makedirs(os.path.dirname(out_folder))
        volatility_distribution_plots.save(
            f"{out_folder}/volatility_distribution_plots.png", scale_factor=5.0
        )
        sectors_volatility_distribution_plots.save(
            f"{out_folder}/sectors_volatility_distribution_plots.png", scale_factor=5.0
        )
        stocks_prices_searchvols_reg.save(
            f"{out_folder}/stocks_prices_searchvols_reg.png", scale_factor=5.0
        )
        sectors_stocks_prices_searchvols_reg.save(
            f"{out_folder}/sectors_stocks_prices_searchvols_reg.png", scale_factor=5.0
        )


if __name__ == "__main__":
    main(opt["--in_file"], opt["--out_folder"])
