import time
from time import gmtime, strftime
from datetime import datetime, timedelta
desired_time = datetime.strptime("23:50", "%H:%M")
import sys

# desired_time = datetime.now().strptime(strftime("%H:%M", gmtime()), "%H:%M")

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
    from webdriver_manager.chrome import ChromeDriverManager ##20230813
    from selenium.webdriver.common.by import By ##20230813
    from seleniumwire import webdriver ##20230813


    import os
    import pandas as pd
    import numpy as np
    import glob


    import pandas as pd
    import pandas as pd
    import requests
    import urllib.request
    import time
    from bs4 import BeautifulSoup
    from datetime import date
    import time
    # from selenium import webdriver
    from selenium.webdriver.common.by import By
    # dr = webdriver.Chrome()


    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait

    ##20230813
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    ##20230813

    sel_options = {
        'proxy': {
            'http': 'http://hamrrgop:o5pgd5udin8t@119.42.38.6:6188',
            'https': 'https://hamrrgop:o5pgd5udin8t@119.42.38.6:6188',
        }
    }

    dr = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options, seleniumwire_options=sel_options) ##20230813
    

    start = time.time()


    # #2) For shortlisted stock

    df_indicator = pd.DataFrame()
    start = time.time()

    filtered_list = ['all-time-high',
    'bollinger-band-breakout',
    'near-support',
    'smart-money',
    'tplus',
    'blue-chip-uptrend',
    'erp5-momentum',
    'increasing-ttm-ichimoku',
    '3-ducks',
    'ema5-cross-sma10',
    'ema5-cross-sma9',
    'ema7-cross-sma200',
    'kelia-ma-cross',
    'sma20-cross-sma40',
    'ma20-cross-ma50',
    'ma30-cross-ma200',
    'ma7-cross-ma26',
    'above-ma50',
    'ma20',
    'ma200',
    'ma5',
    'ma50',
    'solid-ma-uptrend',
    'bollinger-band-squeeze',
    'bollinger-band-swing',
    'ichimoku-above-kumo',
    'ichimoku-bearish-reversal',
    'ichimoku-bullish-reversal',
    'ichimoku-chikou-span-cross',
    'ichimoku-kijun-sen-cross',
    'ichimoku-kumo-breakout',
    'ichimoku-kumo-twist',
    'tenkan-kijun-cross',
    'macd-4r1g-above-signal',
    'macd-above-0',
    'macd-cross-0',
    'parabolic-sar',
    'rsi-above-50',
    'simple-uptrend',
    'stochastic-overbought',
    'bollinger-band-oversold',
    'cci-cross',
    'macd-oversold',
    'oversold-bullish-engulfing',
    'rsi-oversold',
    'short-term-oversold',
    'stochastic-oversold',
    'lower-high-lower-low',
    '20-day-high',
    '52-week-high',
    '52-week-low',
    'fbo-almost',
    'fbo-recent',
    'tplus-volume',
    'bullish-candlestick',
    'candle-4r1g',
    'gap-up',
    'heikin-ashi-4g1r',
    'heikin-ashi-4r1g',
    'heikin-ashi-strong-buying-pressure',
    'heikin-ashi-strong-selling-pressure',
    'ikh-ha-strong-buying-pressure',
    'ikh-ha-strong-selling-pressure',
    'chaikin-money-flow-cmf',
    'on-balance-volume-obv',
    'silence-is-golden',
    'volume-engulfing',
    'volume-increase-30-percent',
    'long-term-sideway',
    'mid-term-sideway',
    'short-term-sideway',
    'gann-square-of-nine',
    'ma-as-support',
    'ma20-as-support',
    'atr',
    'risk-reward-ratio-chandelier-exit',
    'sharpe-ratio',
    'vwma-as-support',
    ]

    # dr = webdriver.Chrome()

    url =[]

    for i in filtered_list:
        website_url = ('https://www.isaham.my/screener/'+i)
        url.append(website_url)

    frames = []

    # Start Looping
    yy = -1
    for cl,link in enumerate(url):
        print ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") 
        print (url[cl])
        dr.get(url[cl])

        time.sleep(0.0005)
        temp_list = [] 
        soup = BeautifulSoup(dr.page_source,'lxml')
        for table in soup.find_all('tbody'):
            for div_class in table.find_all('div', {'class':'d-flex flex-row align-items-center'}):
                for i,j in enumerate (div_class.find_all('div')[1]):
                    if i == 0:
                        temp_list.append(j.text)
                        # print (temp_list)
        
        time.sleep(0.0005)
                    
        while True:
            try:
                
                dr.find_element(By.XPATH, "/html/body/div/div[5]/div/div[2]/div[1]/ul/li[9]/a").click()
                # WebDriverWait(dr, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[5]/div/div[2]/div[1]/ul/li[9]/a"))).click()
                soup1 = BeautifulSoup(dr.page_source,'lxml')
                time.sleep(0.0005)
                for table in soup1.find_all('tbody'):
                    for div_class in table.find_all('div', {'class':'d-flex flex-row align-items-center'}):
                        for i,j in enumerate (div_class.find_all('div')[1]):
                            if i == 0:
                                temp_list.append(j.text)
                                # print (temp_list)


            except:
                break

        
        yy = yy + 1

        df_staging = pd.DataFrame(temp_list, columns =['stock'])
        df_staging['indicator'] = link[31:]

        df_indicator = pd.concat([df_indicator, df_staging], ignore_index=True)


    # 3) Append all the information into a single data frame.
        

    df_indicator['date'] = date.today()
    df_indicator['stock'] = df_indicator['stock'].str.replace('N/A','NA')
    df_indicator.to_csv(f'stock_list_{date.today()}.csv')
    df_indicator.info()


    end = time.time()

    print("The time of execution of above program is :",
        (end-start), "s")

    ## write to Azure Table
    from azure.cosmosdb.table.tableservice import TableService 
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
    TOLOADINTOTABLE = "dailyshortlistedraw"

    date_today = date.today().strftime('%Y-%m-%d')

    def doLoad(ts):
        df = df_indicator.copy()
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        df['PartitionKey'] = date_today
        # df['PartitionKey'] = pd.to_datetime(df[f'{prefix}date']).dt.strftime('%Y%m%d').astype('int')
        
        df= df.to_dict('records')
        rows = [row for row in df]    
        for row in rows:
            a = row['PartitionKey']
            row['PartitionKey'] = a
            row['RowKey'] = row['stock'] + '_for_' + row['indicator']
            ts.insert_or_replace_entity(TOLOADINTOTABLE, row)

    table_service = TableService(connection_string=CONNECTION_STRING)
    table_service.create_table(TOLOADINTOTABLE)
    doLoad(table_service)

    print ("Done load shortlisted raw to Azure Table")
    
    
    

    ##clean and write to Azure Table Again

    indicators = ['20-day-high',
    '3-ducks',
    '52-week-high',
    '52-week-low',
    'above-ma50',
    'all-time-high',
    'atr',
    'blue-chip-uptrend',
    'bollinger-band-breakout',
    'bollinger-band-oversold',
    'bollinger-band-squeeze',
    'bollinger-band-swing',
    'bullish-candlestick',
    'candle-4r1g',
    'cci-cross',
    'chaikin-money-flow-cmf',
    'ema5-cross-sma10',
    'ema5-cross-sma9',
    'ema7-cross-sma200',
    'erp5-momentum',
    'fbo-almost',
    'fbo-recent',
    'gann-square-of-nine',
    'gap-up',
    'heikin-ashi-4g1r',
    'heikin-ashi-4r1g',
    'heikin-ashi-strong-buying-pressure',
    'heikin-ashi-strong-selling-pressure',
    'ichimoku-above-kumo',
    'ichimoku-bearish-reversal',
    'ichimoku-bullish-reversal',
    'ichimoku-chikou-span-cross',
    'ichimoku-kijun-sen-cross',
    'ichimoku-kumo-breakout',
    'ichimoku-kumo-twist',
    'ikh-ha-strong-buying-pressure',
    'ikh-ha-strong-selling-pressure',
    'increasing-ttm-ichimoku',
    'kelia-ma-cross',
    'long-term-sideway',
    'lower-high-lower-low',
    'ma-as-support',
    'ma20',
    'ma20-as-support',
    'ma20-cross-ma50',
    'ma200',
    'ma30-cross-ma200',
    'ma5',
    'ma50',
    'ma7-cross-ma26',
    'macd-4r1g-above-signal',
    'macd-above-0',
    'macd-cross-0',
    'macd-oversold',
    'mid-term-sideway',
    'near-support',
    'on-balance-volume-obv',
    'oversold-bullish-engulfing',
    'parabolic-sar',
    'risk-reward-ratio-chandelier-exit',
    'rsi-above-50',
    'rsi-oversold',
    'sharpe-ratio',
    'short-term-oversold',
    'short-term-sideway',
    'silence-is-golden',
    'simple-uptrend',
    'sma20-cross-sma40',
    'smart-money',
    'solid-ma-uptrend',
    'stochastic-overbought',
    'stochastic-oversold',
    'tenkan-kijun-cross',
    'tplus',
    'tplus-volume',
    'volume-engulfing',
    'volume-increase-30-percent',
    'vwma-as-support']

    #Load Screened Stock Dataset  
    # df = pd.read_csv(f'stock_list_{date_shortlisted}.csv', usecols=range(1,4))
    # df = df[df['date'] == date_shortlisted]
    df1 = df_indicator.copy()

    del df_indicator
    
    df1 = df1[['stock', 'date', 'indicator']]

    shortlisted1 = pd.crosstab([df1['date'], df1['stock']], df1['indicator'], dropna=False)
    shortlisted1.reset_index(inplace = True)
    shortlisted1

    col_reindex = ['date', 'stock'] + indicators


    df1 = shortlisted1.reindex(col_reindex, axis='columns').fillna(0)
    
    del shortlisted1
    
    df1

    # Remove symbol, indication of if a stock is Shariah, etc. 

    #For Shortlisted Stock Dataset
    df1['name'] = df1['stock'].str.strip('*')
    df1['name'] = df1['name'].str.replace("( ).*","")

    df1.columns = df1.columns.str.replace("-", "_")

    prefix = 'dailyraw_'
    df1 = df1.add_prefix(prefix)

    df1 = df1.reset_index()



    # Load to Azure Table
    from azure.cosmosdb.table.tableservice import TableService 
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
    TOLOADINTOTABLE = "dailyshortlistedclean"

    date_today = date.today().strftime('%Y-%m-%d')

    def doLoad(ts):
        df = df1.copy()
        df[f'{prefix}date'] = pd.to_datetime(df[f'{prefix}date']).dt.strftime('%Y-%m-%d')
        df['PartitionKey'] = date_today
        
        df= df.to_dict('records')
        rows = [row for row in df]    
        for row in rows:
            a = row['PartitionKey']
            row['PartitionKey'] = a
            row['RowKey'] = row[f'{prefix}name']
            ts.insert_or_replace_entity(TOLOADINTOTABLE, row)

    table_service = TableService(connection_string=CONNECTION_STRING)
    table_service.create_table(TOLOADINTOTABLE)
    doLoad(table_service)

    print ("Done load shortlisted clean to Azure Table")
   
    
    ## Stock Price

    url =[]


    for i in range(1,49):
        website_url = (f'https://www.bursamalaysia.com/market_information/equities_prices?page={i}&per_page=50')
        url.append(website_url)
        
    print (url)

    import datetime
    frames = []

    for link in url:
        dr.get(link)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        # dr = requests.get(link)
        # print (dr.page_source)
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
    stock_list.columns = ['name', 'code', 'lacp']

    stock_list['date'] = date.today()

    end = time.time()

    stock_list.info()

    print("The time of execution of above program is :",
        (end-start), "s")

    
    dr.quit()



    from azure.cosmosdb.table.tableservice import TableService 
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
    TOLOADINTOTABLE = "dailystockprice"

    date_today = date.today().strftime('%Y-%m-%d')

    def doLoad(ts):
        df = stock_list.copy()
        df[f'date'] = pd.to_datetime(df[f'date']).dt.strftime('%Y-%m-%d')
        df['PartitionKey'] = date_today
        
        df= df.to_dict('records')
        rows = [row for row in df]    
        for row in rows:
            a = row['PartitionKey']
            row['PartitionKey'] = a
            row['RowKey'] = row[f'name']
            ts.insert_or_replace_entity(TOLOADINTOTABLE, row)

    table_service = TableService(connection_string=CONNECTION_STRING)
    table_service.create_table(TOLOADINTOTABLE)
    doLoad(table_service)

    print ("Done load to stock price to Azure Table")



    ###########################################################################################################
    ##### Score model
    #####
    #####
    ###########################################################################################################

    import warnings
    warnings.filterwarnings('ignore')
    
    # General Purpose Modules
    import pickle
    from datetime import datetime
    
    # Data Processing Modules
    import numpy as np
    import pandas as pd
    
    # ML Modules
    import lightgbm as lgb
    from sklearn.preprocessing import OrdinalEncoder
    from sklearn.metrics import roc_auc_score,precision_score, recall_score 
    from sklearn.linear_model import LogisticRegression
    
    # Custom modules
    from dataset_schema_dict import dataset_schema
    
    # Script variables
    pd.options.mode.chained_assignment = None
    
    _author = 'amirul'
    
    script_start = datetime.now()       # Script start
    
    _seed = 999                         # random state seed
    
    save_transformers = True            # Save the lgb transformers
    
    verbose_script = True               # Verbosity of script
    
    dict_path = f'./python_model_objects/'
    f_name = dict_path + f'dataset_schema_dict.pkl'
    
    # Load from pickle into __main__
    with open(f_name, 'rb') as handle:
        dataset_schema = pickle.load(handle)
    
    
    path = f'./python_model_objects/'
    
    verbose_script = False
    
    mdl_f_name = path + f'd3_p3_lgbmcv_model.pkl'
    
    # Load from pickle into __main__
    with open(mdl_f_name, 'rb') as handle:
        lgb_classifier = pickle.load(handle)
    
    
    # Set aside feature names
    feature_names = lgb_classifier.feature_name
    
    df = df1.copy()
    df.columns = df.columns.str.removeprefix("dailyraw_")
    df.columns = df.columns.str.replace("_", "-")
    df = df.reset_index()
    df[indicators] = df[indicators].astype('category')
    
    
    stock_list['name_new'] = stock_list['name'].str.strip('*')
    stock_list['name_new'] = stock_list['name_new'].str.replace("( ).*","")
    stock_list['date_new'] = stock_list['date']
    stock_list['t0'] = stock_list['lacp']
    stock_list_new = stock_list[['date_new','name_new', 't0']]
    stock_list_new

    del stock_list
            
    df = df.merge(stock_list_new, how='left', left_on='name', right_on = 'name_new')

    del stock_list_new
    del df1
    
    df['day_name'] = pd.to_datetime(df['date'], format='%Y-%m-%d').dt.day_name()
    df['month'] = pd.to_datetime(df['date'], format='%Y-%m-%d').dt.strftime('%m')

    col_to_use = feature_names + ['name', 'date']
    df = df[col_to_use]
      
    
    print (df.columns)

    df.head(10).to_csv('df_sample_10.csv')
    #df = df.astype(dataset_schema)
    df = df.astype({
          '20-day-high': 'object',
          '3-ducks': 'object',
          '52-week-high': 'object',
          '52-week-low': 'object',
          'above-ma50': 'object',
          'all-time-high': 'object',
          'atr': 'object',
          'blue-chip-uptrend': 'object',
          'bollinger-band-breakout': 'object',
          'bollinger-band-oversold': 'object',
          'bollinger-band-squeeze': 'object',
          'bollinger-band-swing': 'object',
          'bullish-candlestick': 'object',
          'candle-4r1g': 'object',
          'cci-cross': 'object',
          'chaikin-money-flow-cmf': 'object',
          'ema5-cross-sma10': 'object',
          'ema5-cross-sma9': 'object',
          'ema7-cross-sma200': 'object',
          'erp5-momentum': 'object',
          'fbo-almost': 'object',
          'fbo-recent': 'object',
          'gann-square-of-nine': 'object',
          'gap-up': 'object',
          'heikin-ashi-4g1r': 'object',
          'heikin-ashi-4r1g': 'object',
          'heikin-ashi-strong-buying-pressure': 'object',
          'heikin-ashi-strong-selling-pressure': 'object',
          'ichimoku-above-kumo': 'object',
          'ichimoku-bearish-reversal': 'object',
          'ichimoku-bullish-reversal': 'object',
          'ichimoku-chikou-span-cross': 'object',
          'ichimoku-kijun-sen-cross': 'object',
          'ichimoku-kumo-breakout': 'object',
          'ichimoku-kumo-twist': 'object',
          'ikh-ha-strong-buying-pressure': 'object',
          'ikh-ha-strong-selling-pressure': 'object',
          'increasing-ttm-ichimoku': 'object',
          'kelia-ma-cross': 'object',
          'long-term-sideway': 'object',
          'lower-high-lower-low': 'object',
          'ma-as-support': 'object',
          'ma20': 'object',
          'ma20-as-support': 'object',
          'ma20-cross-ma50': 'object',
          'ma200': 'object',
          'ma30-cross-ma200': 'object',
          'ma5': 'object',
          'ma50': 'object',
          'ma7-cross-ma26': 'object',
          'macd-4r1g-above-signal': 'object',
          'macd-above-0': 'object',
          'macd-cross-0': 'object',
          'macd-oversold': 'object',
          'mid-term-sideway': 'object',
          'near-support': 'object',
          'on-balance-volume-obv': 'object',
          'oversold-bullish-engulfing': 'object',
          'parabolic-sar': 'object',
          'risk-reward-ratio-chandelier-exit': 'object',
          'rsi-above-50': 'object',
          'rsi-oversold': 'object',
          'sharpe-ratio': 'object',
          'short-term-oversold': 'object',
          'short-term-sideway': 'object',
          'silence-is-golden': 'object',
          'simple-uptrend': 'object',
          'sma20-cross-sma40': 'object',
          'smart-money': 'object',
          'solid-ma-uptrend': 'object',
          'stochastic-overbought': 'object',
          'stochastic-oversold': 'object',
          'tenkan-kijun-cross': 'object',
          'tplus': 'object',
          'tplus-volume': 'object',
          'volume-engulfing': 'object',
          'volume-increase-30-percent': 'object',
          'vwma-as-support': 'object',
          't0': np.float32,
          'day_name': 'object',
          'month': 'object',
          'name': 'object',
          'date': 'object',})
    
    df.set_index(['name', 'date'], inplace=True)
    
    print(df.dtypes)
    
    for col in df.columns:
        if df[col].dtype == object or df[col].dtype.name == 'category':
            if verbose_script:
                print('encoding categorical column:')
                print(col)
                print('')
    
            # Fill missing values
            df[col].fillna('__unk__', inplace = True)
    
            # Load ...
            enc_f_name = path + f'ordEnc_{col}.pkl'
            with open(enc_f_name, 'rb') as handle:
                encoder = pickle.load(handle)
    
            # Transform the df object values
            new_values = encoder.transform(df[col].to_numpy().reshape(-1,1))
            
            df[col] = pd.Categorical(new_values.ravel(), ordered = False)
    
    
    scenario_list = ['d3_p3','d3_p5', 'd3_p7', 'd5_p3', 'd5_p5', 'd5_p7', 'd7_p3', 'd7_p5', 'd7_p7']
    
    df_score = pd.DataFrame()
    # list_df = []
    for i in scenario_list:
        mdl_f_name = path + f'{i}_lgbmcv_model.pkl'
    
        # Load from pickle into __main__
        with open(mdl_f_name, 'rb') as handle:
            lgb_classifier = pickle.load(handle)
    
        # Set aside feature names
        feature_names = lgb_classifier.feature_name
        
        df_staging = df.copy()
    
        df_staging['y_pred'] = lgb_classifier.predict_proba(df_staging[feature_names])[:,1]
       
        df_staging.reset_index(inplace=True)
        
        df_staging['scenario'] = i

        print ('Scoring for {i}')
        
        df_concat = df_staging[['name', 'date', 'y_pred', 'scenario']]

        # list_df.append(df_concat)
        df_score = pd.concat([df_score, df_concat], ignore_index=True)
        del df_concat
    
    del df
    del df_staging
    

    df_score.info()
    df_score['id_scored'] = df_score['name'] + '_for_' +df_score['scenario']
    con_high = df_score['y_pred'] > 0.9
    con_med = df_score['y_pred'] > 0.8
    
    con = [con_high, con_med]
    
    choices = ['High', 'Medium']
    
    df_score['band'] = np.select(con, choices, "Low")

    df_score = df_score[df_score['band'].isin(['High','Medium'])]
    
    ## Write to Azure Table
    from azure.cosmosdb.table.tableservice import TableService 
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
    TOLOADINTOTABLE = "dailyscorednew"
    
    date_today = date.today().strftime('%Y-%m-%d')
    
    def doLoad(ts):
        df = df_score.copy()
        df[f'date'] = pd.to_datetime(df[f'date']).dt.strftime('%Y-%m-%d')
        df['PartitionKey'] = date_today
        
        df= df.to_dict('records')
        rows = [row for row in df]    
        for row in rows:
            a = row['PartitionKey']
            row['PartitionKey'] = a
            # row['RowKey'] = row[f'name']
            row['RowKey'] = row[f'id_scored'] 
            ts.insert_or_replace_entity(TOLOADINTOTABLE, row)
    
    table_service = TableService(connection_string=CONNECTION_STRING)
    table_service.create_table(TOLOADINTOTABLE)
    doLoad(table_service)
    
    print ("Done load scored data to Azure Table")


    ##################################################################################################################################################################


while True:
    now = datetime.now().strptime(strftime("%H:%M", gmtime()), "%H:%M")
    # if desired_time == now:
    #     print (now)
    #     print ("Scoring run......")
    #     main()
    #     # time.sleep(30)
    if now == now:
        print (now)
        print ("Scoring run......")
        main()
        print ("Done scoring......")
        sys.exit()
    else:
        # now = datetime.now().strptime(strftime("%H:%M", gmtime()), "%H:%M")
        # difference = desired_time - now
        # seconds = difference.total_seconds()
        # print (f'Sleeping for {seconds} seconds')
        # time.sleep(abs(seconds)*0.1)
        # break
        sys.exit()








