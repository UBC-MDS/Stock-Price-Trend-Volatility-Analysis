# Stock-Price-Trend-Volatility-Analysis
Assessing associations between stock return volatility and search trend volatility

## Public Dataset

We will be analysing the standard deviation of weekly search trends and weekly returns over a one-year period July 2020 to July 2021.

We will be using Yahoo Finance data for obtaining stock volatility information. Yahoo Finance data is available at https://ca.finance.yahoo.com/lookup 

For trend volatility information, we will be using data publically available through Google Trends https://trends.google.com/trends/ 

We have provided a script to download the final data. You may find this script in our repository in the src folder.

Putting the dataset together requires running a few scripts to transform and merge data prior to running the download script. You must run the gt-file-downloader-source.py and yf-file-downloader-source.py files to create directories with csvs for all stock tickers. Then, run stocks-price-merge.py and stocks-trends-merge.py to concatenate the stock data into one file each for returns and trends. Finally, price_trend_merger.py will merge all data into a file which is ready for analysis.

## Research Question

Our inferential research question is:

```Is there an association between weekly google trends search volatility and weekly stock return volatility?```

The motivation for this question is that there are certain derivative trading strategies that revolve around being able to benefit from increases or decreases in the implied volatility of the underlying stock.

Please note that we may refine this question to be specific to certain stock classes. To start, we will focus on a random subset of stocks in the S&P 500 for a one year period.

This is an inferential question since we are not attempting to explain causality between the search and price volatility, we are simply searching for correlations. We leave predictive questions for future analysis.

## Data Analysis Plan

We will be using simple linear regression to analyse our data. Our $R^2$ value will be used to assess the strength of association, with domain-dependent interpretation that will follow from future research.

Our data cleaning may involve some cleaning of the returns data, specifically converting returns to percentage formats for standardization.

## EDA
### Table

Our initial EDA table will be a table in which each observation represents a stock, with columns indicating the stock ticker, the standard deviation of weekly returns, and the standard deviation of weekly search trends.

### Figure

Our initial figures will involve histograms of the returns volatility and search trends volatility of all stocks. We will also produce the initial scatter plot and regression line of the data.

### Overall

This combination of table and figures should give us a good overview of the variation in our assessed variables as well as how they are related, and a rough idea of strength of their association.

## Sharing Results

The sharing of the results should be fairly straight-forward. We will likely use a jupyter notebook as it has been highlighted as a good resource for communication. We will provide some basic interpretation of our findings in this notebook. Our github repo can be shared for more technically inclined individuals. Finally, we may use Xaringan as a slideshow format for sharing a presentation of results.
