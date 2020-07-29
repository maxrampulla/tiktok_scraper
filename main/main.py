import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import argparse
import processor


# Note: Scraper is visible so captcha can be mannually performed by user
# (captcha would be promtped only at beginging of the scraping process)
#
# If the scraper does not work, replace Applebot below with:
#   - Bingbot
#   - DuckDuckBot
#   - Naverbot
#   - Twitterbot
#   - Yandex
opts = Options()
opts.add_argument("user-agent=Applebot")


# constructs the argument parser and parses the arguments
def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--input_file", required=True,
                    help="filepath to csv", type=str)
    # ap.add_argument("-n", "--number_of_tiktoks", required=False,
    #                 help="Number of tiktoks parsed (will parse all unless \
    #                 specificed)", type=str)

    args = ap.parse_args()

    return args.input_file,  # args.number_of_tiktoks


# creates dictionary with a csv of all URLS
def url_dict(arguments):

    filepath = arguments[0]
    tiktoks = []

    with open(filepath, 'r') as file:
        for row in file:
            if row.strip()[:4] == "http":
                tiktoks.append(row.strip())

    return tiktoks


# scrapes using selenium
def scraper(tiktoks):
    driver = webdriver.Chrome(options=opts)

    for i in tiktoks:
        # settig user agent
        driver.get(i)

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//h1[@class='jsx-961678791 video-meta-title']")))

            element = driver.find_elements_by_xpath(
                "//h1[@class='jsx-961678791 video-meta-title']")

            for n in element:
                with open('tiktoktext.csv', 'a') as file:
                    file.write('%s\n' % n.text.replace(",", ""))
        except Exception:
            print("\033[91mlink broken:" + " %s" % i)

    driver.close()


if __name__ == "__main__":
    arguments = get_args()
    (scraper(url_dict(arguments)))
    processor.plot(processor.tokenizer('tiktoktext.csv'))
