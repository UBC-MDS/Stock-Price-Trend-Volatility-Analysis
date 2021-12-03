import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd


def get_yahoo_finance_data(terms_file, terms_column):
    data_from_file = pd.read_csv(terms_file)
    terms = list(data_from_file[terms_column])

    # webdriver and download paths
    chrome_webdriver_path = "./chromedriver"
    download_path = "./yahoo-finance-data"

    # webdriver settings
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_path,
        },
    )

    # initialize the webdriver
    driver = webdriver.Chrome(executable_path=chrome_webdriver_path, options=options)

    for term in terms:
        url = f"https://finance.yahoo.com/quote/{term}/history?period1=1593907200&period2=1625097600&interval=1wk&filter=history&frequency=1wk&includeAdjustedClose=true"
        # start driver
        driver.get(url)
        time.sleep(1)
        driver.refresh()  # refresh once in case of page load error
        time.sleep(3)
        download_btn_click = driver.find_element_by_css_selector(
            "[download]"
        ).click()  # download csv file button
        time.sleep(10)

    driver.quit()
    return True


get_yahoo_finance_data("Data_Download_Automation_Src/SP500.csv", "Symbol")
