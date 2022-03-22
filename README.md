# Wazirx-Data-Scrapper - To Scrape Live Crypto Prices From Wazirx
NOTE: This code is for educational purposes only. 

Wazirx is a leading Indian cryptocurrency exchange.
Wazirx already provides api for gathering data : https://docs.wazirx.com/#public-rest-api-for-wazirx
However this code is simple to implement.
Please read wazirx terms and conditions and robot.txt before using the code from https://wazirx.com/
wazirx robot.txt: https://wazirx.com/robots.txt


The exchange url has two parts. The BASE URL and COINPAIR
eg: coinpair in https://wazirx.com/exchange/BTC-INR is BTC-INR.
Find the coinpair you want by visiting wazirx crypto exchange and selecting the coin.

Package versions:
bs4 =='4.10.0'
selenium =='4.1.0'
numpy == '1.20.3'
pandas == '1.3.4'

Additional Requirements:
You need chromedriver.exe and Google Chrome which are compatible with each other.
This program is tested on : Google Chrome, Version 98.0.4758.102 (Official Build) (64-bit) and it's chrome driver
Download compatible chrome driver from : https://chromedriver.chromium.org/downloads 

Further Improvements to be done:
Speedup in phantomJS instead of chromedriver.exe : Reference: https://www.guru99.com/selenium-with-htmlunit-driver-phantomjs.html#:~:text=HtmlUnit%20and%20PhatomJS-,HTMLUnitDriver,known%20as%20Headless%20Browser%20Driver.
multithread for multiple coin pages at once. From a list of coins in coins.config file.
Improve interval capturing system with more accuracy.
Handle exceptions.
Close browser sessions properly

Advanced experimentation:
BS4 is used for parsing the data from selinium. 
Implementing custom parser for the website may reduce lag times due to processing. 
This needs lot of modifications in the code.

Further features to add:
Show warning if internet is very slow or if it is not working.
Telegram api for price alerts.



*** ERROR ***
SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 97
Current browser version is 99.0.4844.82 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe
*** If you are getting error like this, download compatible chrome driver from https://chromedriver.chromium.org/downloads ***
