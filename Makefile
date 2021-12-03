# Stock Price Trend Volatility data pipe
# author : Group 30 - Block 3 - MDS UBC
# date: 2021-12-02

all: data/processed/prices_trends_merged_data.csv data/processed/stocks-prices-trends-change-percentages.csv data/processed/stocks-prices-trend-volatility.csv results/sectors_stocks_prices_searchvols_reg.png results/sectors_volatility_distribution_plots.png results/stocks_prices_searchvols_reg.png results/volatility_distribution_plots.png results/regression-results.txt results/regression-plot.png results/residuals-plot.png doc/Stock_Price_Trend_Volatility_Analysis_report.md doc/Stock_Price_Trend_Volatility_Analysis_report.html

# download data
data/processed/prices_trends_merged_data.csv: src/download-data.py
	python src/download-data.py --url=https://raw.githubusercontent.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis/main/data/prices_trends_merged_data.csv --out_file=data/processed/prices_trends_merged_data.csv

# generate stocks price and trends weekly data
data/processed/stocks-prices-trends-change-percentages.csv: src/generate-stock_price_trend_df.py
	python src/generate-stock_price_trend_df.py --in_file=data/processed/prices_trends_merged_data.csv --out_file=data/processed/stocks-prices-trends-change-percentages.csv

# generate weekly volatility information per stock
data/processed/stocks-prices-trend-volatility.csv: src/generate-stock_price_trend_volatility_df.py
	python src/generate-stock_price_trend_volatility_df.py --in_file=data/processed/stocks-prices-trends-change-percentages.csv --out_file=data/processed/stocks-prices-trend-volatility.csv

# generate generate exploratory data analysis plots
results/sectors_stocks_prices_searchvols_reg.png results/sectors_volatility_distribution_plots.png results/stocks_prices_searchvols_reg.png results/volatility_distribution_plots.png: src/generate-plot-images.py
	python src/generate-plot-images.py --in_file=data/processed/stocks-prices-trend-volatility.csv --out_folder=results

# generate regression results
results/regression-results.txt results/regression-plot.png results/residuals-plot.png: src/SLR.R
	Rscript src/SLR.R --csv_path=data/processed/stocks-prices-trend-volatility.csv

# Create final report
doc/Stock_Price_Trend_Volatility_Analysis_report.md doc/Stock_Price_Trend_Volatility_Analysis_report.html: doc/Stock_Price_Trend_Volatility_Analysis_report.Rmd doc/references.bib
	Rscript -e "rmarkdown::render('doc/Stock_Price_Trend_Volatility_Analysis_report.Rmd', output_format = 'all')"

clean:
	rm -rf data/processed/stocks-prices-trends-change-percentages.csv
	rm -rf data/processed/stocks-prices-trend-volatility.csv
	rm -rf results/sectors_stocks_prices_searchvols_reg.png
	rm -rf results/sectors_volatility_distribution_plots.png
	rm -rf results/stocks_prices_searchvols_reg.png
	rm -rf results/volatility_distribution_plots.png
	rm -rf results/regression-results.txt
	rm -rf results/regression-plot.png
	rm -rf results/residuals-plot.png
	rm -rf doc/Stock_Price_Trend_Volatility_Analysis_report.md
	rm -rf doc/Stock_Price_Trend_Volatility_Analysis_report.html