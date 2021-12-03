Stock Price Trend Volatility Analysis
================
Group30 - Amir Abbas Shojakhani, Julien Gordon, Helin Wang
11/26/2021

-   [Summary](#summary)
-   [Introduction](#introduction)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
-   [Results & Discussion](#results--discussion)
-   [Limitations & Future Research](#limitations--future-research)
    -   [References](#references)

# Summary

In this project, we analyze whether there is any association between the
volatility of weekly Google Trends(official, n.d.a) keyword interest of
a stock ticker and the volatility of weekly stock returns. We analyze
the standard deviation of weekly search trends and weekly returns over a
one-year period July 2020 to July 2021 of over 300 stocks in the S&P
500, ultimately finding a small but statistically significant
association.

# Introduction

Investment firms are increasingly looking to data science and unusual
data sources to provide informational advantages to bolster their
portfolio strategies. In this project, we are investigating whether
Google Trends data on stock ticker names can provide insight into return
volatility. Investors are often interested in understanding the
volatility of stock returns. Some financial derivative trading
strategies try to take advantage of changes in a stocks’ return
volatility, as certain options are sensitive to changes in implied
volatility.

To cover the basics, the term “stock market” typically refers to one of
the major stock market indexes, such as the Dow Jones Industrial Average
or the Standard & Poor’s 500, which includes 500 of the largest U.S.
companies. It is a global network in which individuals can purchase
ownership, commonly known as shares, of a public company. Companies will
become public when they are listed under a stock exchange where the
financial instruments are bought and sold. Moreover, a financial
[derivative](https://www.investopedia.com/terms/d/derivative.asp) is a
product or contract which typically derives its value from an underlying
asset, such as an
[option](https://www.investopedia.com/terms/o/option.asp) on a company’s
stock. One property of many option derivatives is option
[vega](https://www.investopedia.com/terms/v/vega.asp), which generally
refers to the sensitivity of the option price to the implied volatility
of the underlying. Some derivative trading strategies revolve around
benefiting from increases or decreases in the implied volatility of the
underlying stock. These properties underscore the motivation for seeking
out associations between unusual data sources and return volatility.

This report was compiled using an R markdown document from R(R Core Team
2021) with scripts running via `docopt` package(de Jonge 2020). The data
tables are stored as .csv files in
[data](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/tree/main/data)
folder. Intermediate analysis is carrying by using `Pandas`(McKinney
2010) package in python(Python Core Team 2019). The final data set that
we use for analysis is displayed by using `kable` function in
`knitr`(Xie, n.d.) package. The results are showing as .png pictures
stored in
[results](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/tree/main/results)
folder and is displayed by applying `knitr` as well.

# Methods

## Data

We use Selenium(Salunke 2014) to automate the process of downloading
stocks prices from Yahoo Finance(official, n.d.b) and their search
interest index from Google Trends. In the src folder, we provide the
automation python files that we used to extract and ultimately merge
these data sources.

We used Pandas-Profiling(Brugman 2019) to get a first at the original
data set. There are 5 features and total 17472 observations with no
missing or duplicate values. `weekly_interest` refers to the interest
over time data from Google Trends, which is the number of search
interests of stocks (symbol variable). This number is relative to the
highest point for the given period. A value of 100 is the peak
popularity for the term and a value of 50 means that the term is half as
popular, and a score of 0 means there was not enough data for this term.
In addition, there are 52 consecutive weeks and 336 different stocks
taken into the data set.

Our data cleaning process involved:

-   Converting weekly absolute returns to percent return formats for
    normalization, which corresponds to the percent return one would
    have received that week owning the stock

-   Transforming weekly search index values to a percent of total index
    search values for that stock, which corresponds to a percent of
    yearly search volume per week

We then take the standard deviation of all of the weekly values by
stock, so that our final dataset is one row per stock. The following
table is a sample of 10 rows of data which is ultimately used for our
analysis. The full data set can be found
[here](https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/blob/main/data/stocks-prices-trend-volatility.csv).

| symbol | Sector                 | price_change_pct | pct_period_search_vol |
|:-------|:-----------------------|-----------------:|----------------------:|
| AAL    | Industrials            |        0.0628100 |             0.8109703 |
| AAP    | Consumer Discretionary |        0.0378506 |             0.5210795 |
| AAPL   | Information Technology |        0.0410338 |             0.8915568 |
| ABBV   | Health Care            |        0.0307708 |             0.8473470 |
| ABC    | Health Care            |        0.0359477 |             0.2220668 |
| ABMD   | Health Care            |        0.0474028 |             2.4691348 |
| ABT    | Health Care            |        0.0275525 |             0.8239577 |
| ACN    | Information Technology |        0.0271709 |             0.6953271 |
| ADBE   | Information Technology |        0.0395646 |             0.9256184 |
| ADI    | Information Technology |        0.0343544 |             0.6095752 |

Table 1. The volatility of stock prices and stock symbol search
interests trends(first 10 rows).

## Analysis

In order to assess the inferential question of the association between
stock return volatility and search trend volatility, we analyse the
standard deviation of weekly search trends and weekly returns for over
300 stocks in the S&P 500 over a one-year period from July 2020 to July
2021. We conduct a simple linear regression (SLR) with a confidence
level of 0.95 with the return volatility as the dependent variable and
search trends volatility as the independent variable. Our null
hypothesis is that there is no association between the two volatilities,
with the alternative being that there is an association. Please note
that we are not testing causality between the search and price
volatility, we only focus on the association. We leave causal analysis
for future research. We use *R*<sup>2</sup> to assess how much variation
in the data our model is explaining, and use a *p* − *v**a**l**u**e*
compared to a 0.05 significance level to decide on whether we may reject
the null hypothesis.

The following plot show the distributions of price change volatility and
stock search volume volatility for all stocks in the data. We see a
right skewed normal shape for price change volatility and more of an
exponential distribution for search volume volatility.

<img src="../results/volatility_distribution_plots.png" title="Figure 1. Right skewed distribution of volatility for both stock price change and stock symbol searching volumn in histogram plots" alt="Figure 1. Right skewed distribution of volatility for both stock price change and stock symbol searching volumn in histogram plots" width="100%" />

Now we have the distributions by different sectors(different
industries):

<img src="../results/sectors_volatility_distribution_plots.png" title="Figure 2. Nearly all distributions of the volatility for both stock price change and stock symbol searching volumn by different industries are similar to the overall ones." alt="Figure 2. Nearly all distributions of the volatility for both stock price change and stock symbol searching volumn by different industries are similar to the overall ones." width="100%" />

Above we plot histograms of the standard deviations of returns and
trends of around 330 stocks selected from the S&P500. We broadly observe
that within the subsectors, the distribution of volatility is fairly
similar to the overall distributions for both return and search
volatility.

# Results & Discussion

Here is the statistical regression results:

    ## 
    ## Regression Results
    ## =================================================
    ##                           Dependent variable:    
    ##                       ---------------------------
    ##                            price_change_pct      
    ## -------------------------------------------------
    ## pct_period_search_vol           0.002**          
    ##                                 (0.001)          
    ##                                                  
    ## Constant                       0.038***          
    ##                                 (0.001)          
    ##                                                  
    ## -------------------------------------------------
    ## Observations                      336            
    ## R2                               0.015           
    ## Adjusted R2                      0.012           
    ## Residual Std. Error        0.013 (df = 334)      
    ## F Statistic              4.932** (df = 1; 334)   
    ## =================================================
    ## Note:                 *p<0.1; **p<0.05; ***p<0.01

In addition, the following two figures are plotted regression results
and plotted residuals.

<img src="../results/regression-plot.png" title="Figure 3. Regression result of showing a relationship between stock symbol search and stock weekly return, but with a very low score of R^2" alt="Figure 3. Regression result of showing a relationship between stock symbol search and stock weekly return, but with a very low score of R^2" width="50%" />

<img src="../results/residuals-plot.png" title="Figure 4. Residuals are not seemingly abnormally distributed." alt="Figure 4. Residuals are not seemingly abnormally distributed." width="50%" />

Given that our p-value of 0.027 for our slope coefficient is less than
our significance level of 0.05, we find a significant coefficient of
trend volatility and reject the null hypothesis in favour of the
alternative. The *R*<sup>2</sup> value of 0.015 indicates that our
simple model is explaining very little of the variation in return
volatility, but more work needs to be done to assess how this compares
to other modelling done in the financial domain. Moreover, the effect
size seems to be fairly small in relation to the range of return
volatility that we observe in the data, but we leave formal analysis of
effect size for future iterations of this project.

Our residual plot demonstrates that our residuals are not seemingly
abnormally distributed. We see broad normal distribution around 0 given
search volatility, and we do not observe any obvious change in variance
or direction of residuals across the plot. This means that it is
unlikely we have meaningfully violated regression assumptions.

<img src="../results/sectors_stocks_prices_searchvols_reg.png" title="Figure 5. Various regression results for volatility by sectors (industry fields), the plot of Communication Services shows strong relationship and the plots of some other sectors even show negative relationships." alt="Figure 5. Various regression results for volatility by sectors (industry fields), the plot of Communication Services shows strong relationship and the plots of some other sectors even show negative relationships." width="100%" />

Comparing across sectors, while the histogram distributions of
volatility of searches and returns seemed fairly similar to the overall
distribution, it seems as if the same notion does not hold for the
association between variables. Some sectors, such as communication
services, seem to have a much stronger relationship than utilities,
while some sectors even display a negative relationship. It must be
noted that since we slice up our data considerably to perform this
analysis, we should expect more sampling variation. Thus, we do not
formally analyse our data by sector but leave this for future iterations
of the project where we can hopefully collect more data.

# Limitations & Future Research

Our limitations include the fact that we have one year of data and
stocks are selected from one index only. Our analysis thus applies to
this time frame and stock pool and it is unclear whether the
relationship would be robust across different time periods or stock
pools. Moreover, with respect to time, financial analysis done in
industry is often performed in a time series manner. The weekly nature
of our data may have some underlying non-linearity, such as seasonal
changes. Moreover, there may be delay effects between trend and return
volatility. The impacts of the potential non-linearity may have unknown
impacts on the reliability of our analysis. Given our analytical and
capacity limitations, we leave a time series analysis of this
relationship for future research.

Additionally we have limited features in a simple linear regression.
Therefore, a logical next step may be to expand our feature set. For
example, while we use searched stock tickers for this EDA, we can
perhaps use the company names or other adjacent searches in a
multivariate regression for our volatility analysis.

It must be noted again that our simple model is explaining very little
of the variation in return volatility. This caveat is to be expected
considering we are using a very simple model to understand markets which
contain lots of complexity.

Ultimately, this positive result is exciting and warrants future
investigation into the use of Google Trends for Financial Analysis.

## References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandasprofiling2019" class="csl-entry">

Brugman, Simon. 2019. “<span class="nocase">pandas-profiling:
Exploratory Data Analysis for Python</span>.”
<https://github.com/pandas-profiling/pandas-profiling>.

</div>

<div id="ref-docopt" class="csl-entry">

de Jonge, Edwin. 2020. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-mckinney-proc-scipy-2010" class="csl-entry">

McKinney, Wes. 2010. “Data Structures for Statistical Computing in
Python.” In *Proceedings of the 9th Python in Science Conference*,
edited by Stéfan van der Walt and Jarrod Millman, 56–61.
https://doi.org/[ 10.25080/Majora-92bf1922-00a](https://doi.org/ 10.25080/Majora-92bf1922-00a ).

</div>

<div id="ref-googletrends" class="csl-entry">

official. n.d.a. *Google Trends Search*.
<https://trends.google.com/trends/?geo=CA>.

</div>

<div id="ref-yahoofinance" class="csl-entry">

———. n.d.b. *Yahoo Finance Search*. <https://ca.finance.yahoo.com/>.

</div>

<div id="ref-python" class="csl-entry">

Python Core Team. 2019. *<span class="nocase">Python: A dynamic, open
source programming language</span>*. Python Software Foundation.
<https://www.python.org/>.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2021. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-selenium" class="csl-entry">

Salunke, Sagar Shivaji. 2014. *Selenium Webdriver in Python: Learn with
Examples*. 1st ed. North Charleston, SC, USA: CreateSpace Independent
Publishing Platform.

</div>

<div id="ref-knitr" class="csl-entry">

Xie, Yihui. n.d. *Knitr: A General-Purpose Package for Dynamic Report
Generation in r*. <https://yihui.org/knitr/>.

</div>

</div>
