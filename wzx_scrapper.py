# Imports and constants
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import pandas as pd
import datetime, time
from selenium.webdriver.chrome.options import Options

# Constants
chromedrive_path = '' # '' means chromedriver.exe is in the same directory of the python program

class wzx():
    '''
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
    '''
    
    def __init__(self,coinpair = 'BTC-INR',MONITOR=False, DEBUG_MODE=False): 
        #import time
        chrome_options = Options()
        if not MONITOR: chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        url = f'https://wazirx.com/exchange/{coinpair}'
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source,'html.parser')
        self._initialize(DEBUG_MODE=DEBUG_MODE)
        
    def refresh(self, output=False): 
        '''
        For refreshing soup object to refresh the data.
        run refresh before calling other data collecting methods to get live data.
        
        Other uses:
        For error correction. 
        Good as an exception in try, except block.
        '''
        if output:
            d,t = str(datetime.datetime.now()).split()
            tick = time.time()
            self.soup = BeautifulSoup(self.driver.page_source,'html.parser')
            lag = time.time()-tick
            return {'fetch_date':d,'fetch_time':t,'lag_in_sec':lag}
        else: self.soup = BeautifulSoup(self.driver.page_source,'html.parser')
        

    def _initialize(self,tries=0, max_tries=3, DEBUG_MODE=False):
        '''        
        DO NOT CHANGE 'tries' variable default of 0.
        
        max_tries tries max of 3 continuous exceptions by default if error happens.
        The program sleeps for sleep_sec seconds when continuous exception greater than sleep_try_threshold
        
        DEBUG_MODE: To print output of steps
        
        Also access: 
        self.driver for self.driver.close() to end session # close browser
        self.soup to access bs4 soup element.
        '''
        try:
            self.price()
        except:
            if tries<max_tries:
                self.refresh()
                if DEBUG_MODE: print('Try ',tries,' failed.')
                self._initialize(tries=tries+1)
                
    def price(self):
        last_price = float(self.soup.find_all("span", {"class": "jsEvtU"})[0].text.replace("₹",'').replace(',',''))
        volume, high, low = [float(i.text.replace(',','')) for i in self.soup.find_all("span", {"class": "dgrWIb"})]
        price = {'last_price' : last_price,
                'volume' : volume,
                'high' : high,
                'low' : low }
        return price
                    
    def order_book(self, return_order_volume=False):
        '''
        returns market depth and order volume
        market depth is progressive sum of order volume. We can compute order_volume from market depth and vice versa.
        '''
        
        md_mat_buy = []
        for i in self.soup.find_all("tbody", {"class": "buy"})[0].find_all("tr"): # use buy or sell
            buy_vol, buy_price = i.find_all('td')[1:]
            buy_vol, buy_price = (buy_vol.text.replace(',',''),buy_price.text.replace(',',''))
            md_mat_buy.append((float(buy_price), float(buy_vol)))

        md_mat_sell = []
        for i in self.soup.find_all("tbody", {"class": "sell"})[0].find_all("tr"): # use buy or sell
            sell_price, sell_vol, _ = i.find_all('td')[:]
            sell_vol, sell_price = (sell_vol.text.replace(',',''),sell_price.text.replace(',',''))
            md_mat_sell.append((float(sell_price), float(sell_vol)))
            
        self.market_depth_raw = np.hstack((md_mat_buy, md_mat_sell))
        self.market_depth_ = pd.DataFrame(self.market_depth_raw,columns=['buy_price','buy_vol','sell_price','sell_vol'])
        
        if return_order_volume: # market_depth, order_volume
            order_vol_ = self.market_depth_raw.copy()
            order_vol_[:,[1,3]] = order_vol_[:,[1,3]]-np.vstack(([[0,0]],order_vol_[:-1,[1,3]]))
            self.order_vol_ = pd.DataFrame(order_vol_,columns=['buy_price','buy_vol','sell_price','sell_vol'])
            return self.market_depth_, self.order_vol_
        else: return self.market_depth_
                
    def trade_history(self):

        trade_mat = []
        for i in self.soup.find_all("table", {"class": "trade-history"})[0].find_all("tr")[1:]:
            buy_sell_indicator = i.get('refvalue') # buy or sell
            price,volume,time = [txt.text.replace(',','') for txt in i.find_all('td')]
            trade_mat.append((price.replace(',',''), volume,time, buy_sell_indicator)) # removed microseconds

        return pd.DataFrame(trade_mat, columns=['price','volume','time','buy_or_sell_indicator'])
    
    def fetch_all(self):
        '''
        refreshes the page and returns dictionary of dataframes of:
        scrape_info
        price
        market_depth
        order_volume
        trade_history
        '''
        scrape_info = self.refresh(output=True)
        md,ov = self.order_book(return_order_volume=True)
        return { 'scrape_info': pd.DataFrame(scrape_info,index=['value']),
                'price':pd.DataFrame(self.price(),index=['value']),
                'market_depth': md,
                'order_volume': ov,
                'trade_history': self.trade_history()
               }
    def view_details(self, seperator_width=60):
        for k,v in self.fetch_all().items():
            print('-'*seperator_width)
            print(k)
            print(v)
            print('-'*seperator_width)
            
    def close_webdriver(self):
        self.driver.close()
        
        
# Usage eg:
#shib = wzx(coinpair='SHIB-INR', MONITOR=False, DEBUG_MODE=False) 

# Commonly used methods:
#shib.view_details()  
#shib.fetch_all()
#shib.close_webdriver() # To free memory

# See docstrings for more info.
