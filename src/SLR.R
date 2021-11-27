# author: Julien Gordon
# date: 2021-11-25

"This script runs simple linear regression and exports results to results folder.
Usage: SLR.R --csv_path=<csv_path>

Options:
--<csv_path>=<csv_path>   One stock per row csv relative path (this is required)
" -> doc

main <- function(opt) {
  
  print("reading data")
  data <- read_csv(opt$csv_path)
  
  print("conducting lm")
  SLR <- lm(price_change_pct ~ pct_period_search_vol, data)
 
#  makes regression results table 
#  print("making txt regression results")
  stargazer(SLR, type = 'text',
            title='Regression Results',
            out = '../data/regression-results.txt')

  
  # note to save in jupyter notebook use
  # from IPython.display import HTML
  # HTML(filename='../results/SLR-regression-results.html')
 

#  generate regression plot   
#  print("making plot 1")
  plot <- data |> ggplot(aes(x = pct_period_search_vol, y = price_change_pct)) + 
    geom_point() +
    stat_smooth(method = "lm", col = "red") +
    ylab("Return volatility (StDev of Weekly Returns (%))") +
    xlab("Google Search Trend volatility (StDev of weekly % of total search volume)") +
    ggtitle(paste0("Simple linear regression of stock return volatility\nagainst Google Search Volume volatility with R^2 of ", round(summary(SLR)$r.squared, 4))) +
    theme_bw(base_size = 10)

    
#  print("saving plot")  
  ggsave("../results/regression-plot.png")


# add residuals    
# print("adding residuals")  
  data_resid <- data
  data_resid$residuals <- resid(SLR)

# generate and save residual plot    
#  print("making resid plot")
  resid_plot <- data_resid |> ggplot(aes(x = pct_period_search_vol, y = residuals)) +
      geom_point() +
      stat_smooth(method = "lm", col = "red") +
      ylab("Residuals") +
      xlab("Search volatility") +
      theme_bw(base_size = 10) +
      ggtitle("Residuals plot")
  
  print("saving plot")  
  ggsave("../results/residuals-plot.png")
}

print("loading libraries")
library(docopt)
library(tidyverse)
library(stargazer)

print("libraries loaded")

opt <- docopt(doc)

print("docopt function run")

main(opt)