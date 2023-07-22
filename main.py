import time
from time import gmtime, strftime
desired_time = '18:40'

def main():
    import timeit
    import pandas as pd
    import requests
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from datetime import date
    import os
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from seleniumwire import webdriver



    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)


    sel_options = {
        'proxy': {
            'http': 'http://hamrrgop:o5pgd5udin8t@2.56.119.93:5074',
            'https': 'https://hamrrgop:o5pgd5udin8t@2.56.119.93:5074',
        }
    }

    dr = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options, seleniumwire_options=sel_options)

    start = time.time()


    # #2) Create a loop to scrape info in each URL for each page.

    url =[]

    for i in range(1,2):
        website_url = (f'https://www.bursamalaysia.com/market_information/equities_prices?page={i}&per_page=50')
        url.append(website_url)
        

    print (url)

    import datetime
    frames = []

    for link in url:
        dr.get(link)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        #dr = requests.get(link)
        print (dr.page_source)
        soup = BeautifulSoup(dr.page_source,'lxml')
        tableMain = soup.find_all('table', {'class':'table datatable-striped text-center equity_prices_table datatable-with-sneak-peek js-anchor-price-table d-none d-lg-block dataTable no-footer'})
        last_div = None
        for last_div in tableMain:pass
        if last_div:
            table = last_div.getText()
        df = pd.read_html(str(last_div), header=0)
        df[0].rename(index= str, inplace = True)
        frames.append(df[0].assign(date=datetime.datetime(2022, 1, 4)))

    # 3) Append all the information into a single data frame.
        
    stock_list = pd.concat(frames)
    stock_list = stock_list[['Name', 'Code', 'LACP']]

    stock_list['date'] = date.today()
    stock_list.info()
    stock_list.to_csv(f'stock_price_{date.today()}.csv')

    end = time.time()

    print("The time of execution of above program is :",
        (end-start), "s")


    dr.quit()

while True:
    if strftime("%H:%M", gmtime()) == desired_time:
        main()
        time.sleep(60)
    # else:
    #     print ("Not Scraping")








