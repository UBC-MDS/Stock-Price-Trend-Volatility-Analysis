# Summary

In this project, we are trying to analyze whether there any relationship
between the volatility of weekly keyword interest of a stock symbol(on
Google Trends) and the one of the weekly stock return. The keywords
searching interests data is originally from Google Trends(official,
n.d.a), and stock price data is Yahoo Finance(official, n.d.b). By doing
so, We analyze the standard deviation of weekly search trends and weekly
returns over a one-year period July 2020 to July 2021.

# Introduction

The term “stock market” often refers to one of the major stock market
indexes, such as the Dow Jones Industrial Average or the Standard &
Poor’s 500, which includes 500 of the largest U.S. companies. It is a
global network in which individuals can purchase ownership, commonly
known as shares, of a public company. Companies will become public when
they are listed under a stock exchange where the financial instruments
are bought and sold. The motivation for this question is that there are
certain derivative trading strategies that revolve around being able to
benefit from increases or decreases in the implied volatility of the
underlying stock. Investors are often interested in understanding the
volatility of stock returns. Some financial derivative trading
strategies try to take advantage of changes in a stocks’ volatility, as
certain options are sensitive to changes in implied volatility.

This report was compiled using R document with scripts running via
`docopt` package(de Jonge 2020). The data tables are stored as .csv
files in
[data](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/tree/main/data)
folder. Intermediate analysis is carrying by using `Pandas`(McKinney
2010) package in python. The final data set that we use for analysis is
displayed by using `kable` function in `knitr`(Xie, n.d.). The results
are showing as .png pictures stored in
[results](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/tree/main/results)
folder and is displayed by applying `knitr` as well.

# Methods

## Data

Data is originally from Google Trends, Google Finance and Yahoo Finance.

We used Pandas-Profiling(Brugman 2019) to git a first at the original
data set. There are 5 features and total 17472 observations with no
missing value and no duplicate row. `weekly_interest` refers to the
interest over time data from Google Trends, which is the number of
search interests of stocks (symbol variable). This number is relative to
the highest point for the given period. A value of 100 is the peak
popularity for the term and a value of 50 means that the term is half as
popular, and a score of 0 means there was not enough data for this term.
In addition, there are 52 weeks in a row and 336 different stocks taken
into the data set.

Our data cleaning involves some cleaning of the returns data,
specifically converting returns to percentage formats for
standardization.

The following table is a sample of 10 rows of data set that has been
used for our analysis. The full data set can be found
[here](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/blob/main/data/stocks-prices-trend-volatility.csv)

<table>
<caption>Table 1. The volatility of stock prices and trends(first 10 rows).</caption>
<thead>
<tr class="header">
<th style="text-align: left;">symbol</th>
<th style="text-align: left;">Sector</th>
<th style="text-align: right;">price_change_pct</th>
<th style="text-align: right;">pct_period_search_vol</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">AAL</td>
<td style="text-align: left;">Industrials</td>
<td style="text-align: right;">0.0628100</td>
<td style="text-align: right;">0.8109703</td>
</tr>
<tr class="even">
<td style="text-align: left;">AAP</td>
<td style="text-align: left;">Consumer Discretionary</td>
<td style="text-align: right;">0.0378506</td>
<td style="text-align: right;">0.5210795</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AAPL</td>
<td style="text-align: left;">Information Technology</td>
<td style="text-align: right;">0.0410338</td>
<td style="text-align: right;">0.8915568</td>
</tr>
<tr class="even">
<td style="text-align: left;">ABBV</td>
<td style="text-align: left;">Health Care</td>
<td style="text-align: right;">0.0307708</td>
<td style="text-align: right;">0.8473470</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ABC</td>
<td style="text-align: left;">Health Care</td>
<td style="text-align: right;">0.0359477</td>
<td style="text-align: right;">0.2220668</td>
</tr>
<tr class="even">
<td style="text-align: left;">ABMD</td>
<td style="text-align: left;">Health Care</td>
<td style="text-align: right;">0.0474028</td>
<td style="text-align: right;">2.4691348</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ABT</td>
<td style="text-align: left;">Health Care</td>
<td style="text-align: right;">0.0275525</td>
<td style="text-align: right;">0.8239577</td>
</tr>
<tr class="even">
<td style="text-align: left;">ACN</td>
<td style="text-align: left;">Information Technology</td>
<td style="text-align: right;">0.0271709</td>
<td style="text-align: right;">0.6953271</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADBE</td>
<td style="text-align: left;">Information Technology</td>
<td style="text-align: right;">0.0395646</td>
<td style="text-align: right;">0.9256184</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADI</td>
<td style="text-align: left;">Information Technology</td>
<td style="text-align: right;">0.0343544</td>
<td style="text-align: right;">0.6095752</td>
</tr>
</tbody>
</table>

Table 1. The volatility of stock prices and trends(first 10 rows).

## Analysis

Simple linear regression(SLR) is adopted to analyze our data. The null
hypothesis is there is a relationship between the volatility of weekly
keyword interest of a stock symbol(on Google Trends) and the one of the
weekly stock return, which the alternative hypothesis is there is NO
difference between these two parties. We use *R*<sup>2</sup> to check on
the performance of the model, and using *p* − *v**a**l**u**e* in this
model to see whether we can successfully reject the null hypothesis.

Also, please pay attention that since this is an inferential question,
we are not explaining causality between the search and price volatility,
but only focus on the correlations.

The following plot show the distributions of price change volatility and
stock search volume volatility. We can see a right skewed shape of both
distributions.

<img src="../results/volatility_distribution_plots.png" alt="Figure 1. Volatility distribution" width="100%" />
<p class="caption">
Figure 1. Volatility distribution
</p>

Now we have the distributions by different sectors:

<img src="../results/sectors_volatility_distribution_plots.png" alt="Figure 2. Volatility distribution by sectors" width="100%" />
<p class="caption">
Figure 2. Volatility distribution by sectors
</p>

Above we plot histograms of the standard deviations of returns and
trends of around 330 stocks selected from the S&P500.

For the returns, we observe a right-skewed normal distribution. This
means that while relatively normally distributed, there are more
outliers on the right tail of the distribution than a pure normal
distribution.

For the trends, we observe a more normal distribution than for the
returns. There may be some evidence of bi-modality in these data, but it
could simply be an artifact of the bin selection. If bi-modality exists,
there seems to be a smaller cluster of stocks with low trend volatility
and a larger cluster of stocks centred around medium trend volatility.

# Results & Discussion

<img src="../results/regression-plot.png" alt="Figure 3. Regression" width="50%" />
<p class="caption">
Figure 3. Regression
</p>

<img src="../results/residuals-plot.png" alt="Figure 4. Residuals" width="50%" />
<p class="caption">
Figure 4. Residuals
</p>

From the basic regression analysis, we do not observe an obvious trend
in the data. It seems as if information on search trend volatility
provides remarkably little information on the return volatility.

While these results are not promising, as discussed in the project
proposal, we can perhaps assess this relationship on particular clusters
of stocks to see if a relationship exists for certain categories.

<img src="../results/sectors_stocks_prices_searchvols_reg.png" alt="Figure 5. Regression result for volatility by sectors" width="100%" />
<p class="caption">
Figure 5. Regression result for volatility by sectors
</p>

# Limitations & Future

We have very limited features so far. Therefore, one thing We can do is
to expand our features of search volatility. For example, while we use
stock tickers for this EDA, we can perhaps use the company names or
other adjacent searches in our volatility analysis.

# References

Brugman, Simon. 2019. “<span class="nocase">pandas-profiling:
Exploratory Data Analysis for Python</span>.”
<https://github.com/pandas-profiling/pandas-profiling>.

de Jonge, Edwin. 2020. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

McKinney, Wes. 2010. “Data Structures for Statistical Computing in
Python.” In *Proceedings of the 9th Python in Science Conference*,
edited by Stéfan van der Walt and Jarrod Millman, 56–61.
https://doi.org/[ 10.25080/Majora-92bf1922-00a](https://doi.org/ 10.25080/Majora-92bf1922-00a ).

official. n.d.a. *Google Trends Search*.
<https://trends.google.com/trends/?geo=CA>.

———. n.d.b. *Yahoo Finance Search*. <https://ca.finance.yahoo.com/>.

Xie, Yihui. n.d. *Knitr: A General-Purpose Package for Dynamic Report
Generation in r*. <https://yihui.org/knitr/>.
