# Stock-Price-Trend-Volatility-Analysis
Assessing associations between stock return volatility and search trend volatility

## Public Dataset

We will be using Google Finance data for obtaining stock volatility information. Google Finance data is available at https://www.google.com/finance/, but we will be leveraging google sheets integration with Google Finance for ease of access https://support.google.com/docs/answer/3093281?hl=en.

We will be using a script to download data available through google trends. You may find this script in our repository.

Specifically, we will use the standard deviation of daily search trends and daily returns over a one-year period July 2020 to July 2021

## Research Question

Our inferential research question is:

```Is there an association between daily google trends search volatility and daily stock return volatility?```

The motivation for this question is that there are certain derivative trading strategies that revolve around being able to benefit from increases or decreases in the implied volatility of the underlying stock. 

Please note that we may refine this question to be specific to certain stock classes. To start, we will focus on a random subset of stocks in the S&P 500.

This is an inferential question since we are not attempting to explain causality between the search and price volatility, we are simply searching for correlations. We leave predictive questions for future analysis. 

## Data Aanalysis Plan

We will be using simple linear regression to analyse our data. Our R^2 value will be used to assess the strength of association, with domain-dependent interpretation that will follow from future research.

Our data cleaning ma involve some cleaning of the returns data, specifically converting returns to percentage formats for standardization. 

## EDA
### Table

Our initial EDA table will be a table in which each observation represents a stock, with columns indicating the stock ticker, the standard deviation of daily returns, and the standard deviation of daily search trends.

### Figure

Our initial figures will involve individual histograms of the returns and search trends of each stocks. We will also produce the initial scatter plot and regression line of the data.

### Overall

This combination of table and figures should give us a good overview of the variation in our assessed variables as well as how they are related, and a rough idea of strength of their association.

## Sharing Results

The sharing of the results should be fairly straight-forward. We will likely use a jupyter notebook as it has been highlighted as a good resource for communication. We will provide some basic interpretation of our findings in this notebook.
