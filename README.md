# Stock-Price-Trend-Volatility-Analysis

## Project Overview

Investment firms are increasingly looking to data science and unusual data sources to provide informational advantages to bolster their portfolio strategies. In this project, we are investigating whether Google Trends data on stock ticker names can provide insight into return volatility**. Investors are often interested in understanding the volatility of stock returns. Some financial derivative trading strategies try to take advantage of changes in a stocks' volatility, as certain options are sensitive to changes in implied volatility. See a primer on option vega if you are interested! <https://www.investopedia.com/terms/v/vega.asp>

Consider this project a screening exercise for whether Google Trends could be useful in volatility-based trading strategies.

In order to assess the association between stock return volatility and search trend volatility, we analyse the standard deviation of weekly search trends and weekly returns for over 300 stocks in the S&P 500 over a one-year period from July 2020 to July 2021. We conduct a simple linear regression with a confidence level of 0.95 with the return volatility as the dependent variable and search trends volatility as the independent variable. Our null hypothesis is that there is no association between the two volatilities, with the alternative being that there is an association.

Ultimately, we find a significant coefficient of trend volatility and reject the null hypothesis in favour of the alternative. The R^2 value indicates that our simple model is explaining very little of the variation in return volatility. Moreover, the effect size seems to be fairly small in relation to the range of return volatility that we observe in the data. These caveats are to be expected considering we are using a very simple model to understand markets which contain lots of complexity. Nonetheless, this positive result is exciting and warrants future investigation into the use of Google Trends for Financial Analysis.

**Note that in statistical terms, the volatility is simply the standard deviation of returns. <https://www.investopedia.com/terms/v/volatility.asp>

## Report

The final report can be found [here](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/blob/main/doc/Stock_Price_Trend_Volatility_Analysis_report.md)

## Executing the Analysis

Reproducibility of results is of utmost importance in data science. In this section, we provide steps for executing our analysis.

### Dependencies

Firstly, please ensure that your python and R environments have installed the following dependencies.

### Process flow chart

The following figure may be helful to visualize the steps of the analysis

![Flow chart](doc/processing-flowchart.png)

### Execution of scripts

IMPORTANT NOTE

Downloading the data will take several hours to run. We suggest instead skipping to step 5 and using the pre-downloaded data in our repository.

#### Download stock ticker info

1. Firstly you must go to _______ and download the list of S&P 500 stocks and their sectors.

#### Automated download of stock return and trend data

2. Open your terminal and navigate to the src folder of the project that you have forked and cloned.

Execute the following commands in terminal, noting that full download will take several hours.

for Yahoo Finance:

```placeholder```

for Google Trends:

```placeholder```

3. Run the following to merge the folder of csvs

for Yahoo Finance:

```placeholder```

for Google Trends:

```placeholder```

4. Run the following to merge trend, finance, and sector information

```placeholder```

5. Run the following to perform necessary feature transformations. The output will be one row per stock-week.

```placeholder```

6. Run the following to calculate weekly volatility information per stock. The output will be one row per stock.

```placeholder```

7. Run the following to generate exploratory data analysis plots

```placeholder```

8. Run the following to generate regression results

```placeholder```

9. Run the following to generate the final R markdown document and knitted output file

```placeholder```
