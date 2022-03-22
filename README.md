# Wazirx-Data-Scrapper - To Scrape Live Crypto Prices From Wazirx
#### NOTE: This code is for educational purposes only. 


## About
- Wazirx is a leading Indian cryptocurrency exchange. 
- Wazirx already provides api for gathering data : https://docs.wazirx.com/#public-rest-api-for-wazirx
- However this code is simple to implement.
- Please read wazirx terms and conditions and robot.txt before using the code from https://wazirx.com/
- wazirx robot.txt: https://wazirx.com/robots.txt

## Information on finding coinpair
- The exchange url has two parts. The BASE URL and COINPAIR
- eg: coinpair in https://wazirx.com/exchange/BTC-INR is BTC-INR.
- Find the coinpair you want by visiting wazirx crypto exchange and selecting the coin.


## Package versions: Tested versions of packages
- bs4 =='4.10.0'
- selenium =='4.1.0'
- numpy == '1.20.3'
- pandas == '1.3.4'


## Requirements to use the scrapper:

- You need chromedriver.exe and Google Chrome which are compatible with each other.
- This program is tested on : Google Chrome, Version 98.0.4758.102 (Official Build) (64-bit) and it's chrome driver
- Download compatible chrome driver from : https://chromedriver.chromium.org/downloads 


## Further Improvements to be done:

- Speedup in phantomJS instead of chromedriver.exe : Reference: https://www.guru99.com/selenium-with-htmlunit-driver-phantomjs.html#:~:text=HtmlUnit%20and%20PhatomJS-,HTMLUnitDriver,known%20as%20Headless%20Browser%20Driver.
- Multithread for multiple coin pages at once. From a list of coins in coins.config file.
- Improve interval capturing system with more accuracy.
- Testing more and Handle exceptions.
- Close browser sessions properly
- Show warning if internet is very slow or if it is not working. 
- Telegram api for price alerts.

## Advanced experimentation:

- BS4 is used for parsing the data from selinium. Implementing custom parser for the website may reduce lag times due to processing. This needs lot of modifications in the code.


*** IN CASE OF THIS ERROR ***

SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 97
Current browser version is 99.0.4844.82 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe

*** Download compatible chrome driver from https://chromedriver.chromium.org/downloads ***

## Usage Example: With SHIB-INR currency pair
#### shib = wzx(coinpair='SHIB-INR', MONITOR=False, DEBUG_MODE=False) 
    coinpair: default-> 'BTC-INR' : coinpair in https://wazirx.com/exchange/BTC-INR is BTC-INR. 
    Find the coinpair you want by visiting wazirx crypto exchange and selecting the coin.
    
    MONITOR (BOOL): default->False :False will open chrome browser in headless mode (silent) True will open the chrome browser in foreground, 
    DEBUG_MODE: default->False: To get more output.
    
    USAGE: 
    coin = wzx(coinpair= 'SOL-INR') # Loads https://wazirx.com/exchange/SOL-INR for scrapping.
    
    For entire data in one go, use:
    coin.fetch_all()
    
    For individual data:
    coin.price_info()
    coin.market_depth_and_order_volume()
    coin.trade_history()

#### shib.view_details() 

#### shib.fetch_all()
       refreshes the page and returns dictionary of dataframes of:
        scrape_info
        price
        market_depth
        order_volume
        trade_history

shib.price() # To see last price, volume, high and low values
shib.refresh() # To refresh webpage
shib.trade_history() # Last 10 recent trades
shib.order_book() # Market Depth and Order Volume information
shib.close_webdriver() # To free memory
See docstrings for more info.
