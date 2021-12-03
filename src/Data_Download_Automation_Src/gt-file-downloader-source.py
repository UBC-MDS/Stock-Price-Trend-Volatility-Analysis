import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd


def get_google_trends_data(terms_file, terms_column):
    data_from_file = pd.read_csv(terms_file)
    terms = list(data_from_file[terms_column])

    # webdriver and download paths
    chrome_webdriver_path = "./chromedriver"
    download_path = "./google-trends-data"

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
        url = f"https://trends.google.com/trends/explore?cat=7&date=2020-07-01%202021-07-01&q={term}"
        # start driver
        driver.get(url)
        time.sleep(1)
        driver.refresh()  # refresh once in case of page load error
        time.sleep(3)
        download_btn_click = driver.find_element_by_class_name(
            "export"
        ).click()  # download csv file button
        time.sleep(10)

        # rename the downloaded file
        os.rename(
            os.path.join(os.path.relpath(download_path), os.listdir(download_path)[0]),
            os.path.join(os.path.relpath(download_path), f"{term}.csv"),
        )

        time.sleep(2)

    driver.quit()
    return True


get_google_trends_data("Data_Download_Automation_Src/SP500.csv", "Symbol")
