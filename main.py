import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#settig user agent
opts = Options()
opts.add_argument("user-agent=Googlebot")

#creates dictionary with all the urls
tiktoks = []

with open('tiktoks.csv', 'r') as file:
    for row in file:
        if row.strip()[:4] ==  "http":
            tiktoks.append(row.strip())

#scrapes using selenium
driver = webdriver.Chrome(options=opts)

for i in tiktoks:
    driver.get(i)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='jsx-961678791 video-meta-title']")))
        element = driver.find_elements_by_xpath("//h1[@class='jsx-961678791 video-meta-title']")
        for n in element:
            with open('tiktoktext.csv', 'a') as file:
                file.write('%s\n' % n.text.replace(",", ""))
    except:
        print("\033[91mlink broken:" + " %s" %i)

driver.close()
