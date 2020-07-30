# TIKTOK Scraper
[![Python: 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)](#)
[![license: MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

Built to be used with a tiktok data dump which provides a list of all videos ever viewed on the platform. The program takes in this data and processes it for word frequency. 

Note: The script runs at about 44 videos a minute. 

Arguments:
    `-h`: help file of usage of the script
    `-f`: input file name

    Default settings:
    `output_path` is the current directory

    Example:
    ```
    # Takes in a tiktok vide csv and produces a new csv and plots 
    >> python3 main.py -f  /Users/maxrampulla/Documents/Python/tiktok_scraper/tiktokscopy.csv
    ```

Future features:
    - Take out midscript csv conversion 
    - Allows for the input of time limit / number of video limit 

Troubleshoot:
    If tiktok has detected you are a bot check here: https://stackoverflow.com/questions/59277001/selenium-is-not-loading-tiktok-pages
