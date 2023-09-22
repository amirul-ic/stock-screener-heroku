# %%
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import holidays

##################
## Get Business Day ##
##################
start = "2023-01-01"
end = "2023-12-31"

df_holiday = pd.DataFrame()
for year in [2022, 2023]:
    data = ((date, 'holiday') for date in holidays.MY(subdiv='KUL', years=year))
    data = pd.DataFrame(data, columns = ['date', 'type'])
    df_holiday = pd.concat([df_holiday, data], ignore_index=True)

df_holiday

df_dates = pd.DataFrame({'date': pd.date_range(start, end)})

busines_dates = pd.bdate_range(start, end)
weekend = df_dates.loc[~df_dates['date'].isin(busines_dates)]
weekend['type'] = 'weekend'

date_exclude = pd.concat([df_holiday, weekend], ignore_index=True)
date_exclude['exclude'] = 1

date_exclude['date'] = pd.to_datetime(date_exclude['date']).dt.strftime('%Y-%m-%d')

date_exclude = date_exclude.drop_duplicates(subset=['date'], keep='first')
date_exclude

df_dates['date'] = pd.to_datetime(df_dates['date']).dt.strftime('%Y-%m-%d')
data_include = df_dates.merge(date_exclude, how='left', left_on='date', right_on= 'date')
data_include['exclude'] = data_include['exclude'].fillna(0)
data_include = data_include.sort_values(by=['date'])
data_include = data_include[data_include['exclude']==0]
data_include = data_include.reset_index()
data_include = data_include[['date']]

del df_holiday
del df_dates
del busines_dates
del weekend
del date_exclude 
del data

# del data_include

# Fetch today's date
date = datetime.today()
date_today = date.today().strftime('%Y-%m-%d')
data_include['date'] = pd.to_datetime(data_include['date']).dt.strftime('%Y-%m-%d')

end = data_include[data_include['date'] == date_today].index[0]
start = end - 12

date_range = data_include['date'].iloc[start:end,].to_list()
print(date_range)

del data_include

######################
## Get Lead value   ##
######################


from azure.cosmosdb.table.tableservice import TableService
from azure.data.tables import TableClient
from azure.cosmosdb.table.models import Entity

CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
table_service = TableService(connection_string=CONNECTION_STRING)

table_client = TableClient.from_connection_string(conn_str=CONNECTION_STRING, table_name="dailystockprice")
df_master = pd.DataFrame()
for date in date_range:
    my_filter = f"PartitionKey eq '{date}'"
    entities = table_client.query_entities(my_filter)
    df_staging = pd.DataFrame(entities)
    df_master = pd.concat([df_master, df_staging], ignore_index = True)

df_master['name'] = df_master['name'].str.strip('*')
df_master['name'] = df_master['name'].str.replace("( ).*","")
df_master['date_rv1'] = pd.to_datetime(df_master['date'], dayfirst=True).dt.strftime('%Y-%m-%d')
df_master['t0'] = df_master['lacp']
data = df_master[['name', 'date_rv1', 't0']]

del df_master

data = data.sort_values(by=['name', 'date_rv1', 't0'], ascending=False)
data = data.drop_duplicates(subset=['name', 'date_rv1'], keep='first')


for i in range(0,8):
    # y = str(i)
    data[f't{i}'] = data.groupby(['name'])['t0'].shift(i)


data = data[['name', 'date_rv1', 't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']]


data[['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']] = data[['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']].replace('No data available in table', np.nan)


data['target_d3_p3'] = np.where(data['t1']> (1.03*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.03*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.03*data['t0']), 1, 0)))))

data['target_d5_p3'] = np.where(data['t1']> (1.03*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.03*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.03*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.03*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.03*data['t0']), 1, 0)))))))))

data['target_d7_p3'] = np.where(data['t1']> (1.03*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.03*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.03*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.03*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.03*data['t0']), 1 , np.where(data['t5']<(0.97*data['t0']), 0, 
               np.where(data['t6']> (1.03*data['t0']), 1 , np.where(data['t6']<(0.97*data['t0']), 0, 
               np.where(data['t7']> (1.03*data['t0']), 1, 0)))))))))))))

data['target_d3_p5'] = np.where(data['t1']> (1.05*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.05*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.05*data['t0']), 1, 0)))))

data['target_d5_p5'] = np.where(data['t1']> (1.05*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.05*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.05*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.05*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.05*data['t0']), 1, 0)))))))))


data['target_d7_p5'] = np.where(data['t1']> (1.05*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.05*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.05*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.05*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.05*data['t0']), 1 , np.where(data['t5']<(0.97*data['t0']), 0, 
               np.where(data['t6']> (1.05*data['t0']), 1 , np.where(data['t6']<(0.97*data['t0']), 0, 
               np.where(data['t7']> (1.05*data['t0']), 1, 0)))))))))))))


data['target_d3_p7'] = np.where(data['t1']> (1.07*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.07*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.07*data['t0']), 1, 0)))))

data['target_d5_p7'] = np.where(data['t1']> (1.07*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.07*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.07*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.07*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.07*data['t0']), 1, 0)))))))))


data['target_d7_p7'] = np.where(data['t1']> (1.07*data['t0']), 1, np.where(data['t1']<(0.97*data['t0']), 0, 
               np.where(data['t2']> (1.07*data['t0']), 1, np.where(data['t2']<(0.97*data['t0']), 0, 
               np.where(data['t3']> (1.07*data['t0']), 1 , np.where(data['t3']<(0.97*data['t0']), 0, 
               np.where(data['t4']> (1.07*data['t0']), 1 , np.where(data['t4']<(0.97*data['t0']), 0, 
               np.where(data['t5']> (1.07*data['t0']), 1 , np.where(data['t5']<(0.97*data['t0']), 0, 
               np.where(data['t6']> (1.07*data['t0']), 1 , np.where(data['t6']<(0.97*data['t0']), 0, 
               np.where(data['t7']> (1.07*data['t0']), 1, 0)))))))))))))



data['target_price_d3_p3'] = np.where(data['t1']> (1.03*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.03*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.03*data['t0']), ((data['t3']/data['t0'])-1), ((data['t3']/data['t0'])-1))))))

data['target_price_d5_p3'] = np.where(data['t1']> (1.03*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.03*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.03*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.03*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.03*data['t0']), ((data['t5']/data['t0'])-1), ((data['t5']/data['t0'])-1))))))))))

data['target_price_d7_p3'] = np.where(data['t1']> (1.03*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.03*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.03*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.03*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.03*data['t0']), ((data['t5']/data['t0'])-1) , np.where(data['t5']<(0.97*data['t0']), ((data['t5']/data['t0'])-1), 
               np.where(data['t6']> (1.03*data['t0']), ((data['t6']/data['t0'])-1) , np.where(data['t6']<(0.97*data['t0']), ((data['t6']/data['t0'])-1), 
               np.where(data['t7']> (1.03*data['t0']), ((data['t7']/data['t0'])-1), ((data['t7']/data['t0'])-1))))))))))))))

data['target_price_d3_p5'] = np.where(data['t1']> (1.05*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.05*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.05*data['t0']), ((data['t3']/data['t0'])-1), ((data['t3']/data['t0'])-1))))))

data['target_price_d5_p5'] = np.where(data['t1']> (1.05*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.05*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.05*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.05*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.05*data['t0']), ((data['t5']/data['t0'])-1), ((data['t5']/data['t0'])-1))))))))))


data['target_price_d7_p5'] = np.where(data['t1']> (1.05*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.05*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.05*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.05*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.05*data['t0']), ((data['t5']/data['t0'])-1) , np.where(data['t5']<(0.97*data['t0']), ((data['t5']/data['t0'])-1), 
               np.where(data['t6']> (1.05*data['t0']), ((data['t6']/data['t0'])-1) , np.where(data['t6']<(0.97*data['t0']), ((data['t6']/data['t0'])-1), 
               np.where(data['t7']> (1.05*data['t0']), ((data['t7']/data['t0'])-1), ((data['t7']/data['t0'])-1))))))))))))))


data['target_price_d3_p7'] = np.where(data['t1']> (1.07*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.07*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.07*data['t0']), ((data['t3']/data['t0'])-1), ((data['t3']/data['t0'])-1))))))

data['target_price_d5_p7'] = np.where(data['t1']> (1.07*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.07*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.07*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.07*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.07*data['t0']), ((data['t5']/data['t0'])-1), ((data['t5']/data['t0'])-1))))))))))


data['target_price_d7_p7'] = np.where(data['t1']> (1.07*data['t0']), (data['t1']/data['t0'])-1, np.where(data['t1']<(0.97*data['t0']), (data['t1']/data['t0'])-1, 
               np.where(data['t2']> (1.07*data['t0']), ((data['t2']/data['t0'])-1), np.where(data['t2']<(0.97*data['t0']), ((data['t2']/data['t0'])-1), 
               np.where(data['t3']> (1.07*data['t0']), ((data['t3']/data['t0'])-1) , np.where(data['t3']<(0.97*data['t0']), ((data['t3']/data['t0'])-1), 
               np.where(data['t4']> (1.07*data['t0']), ((data['t4']/data['t0'])-1) , np.where(data['t4']<(0.97*data['t0']), ((data['t4']/data['t0'])-1), 
               np.where(data['t5']> (1.07*data['t0']), ((data['t5']/data['t0'])-1) , np.where(data['t5']<(0.97*data['t0']), ((data['t5']/data['t0'])-1), 
               np.where(data['t6']> (1.07*data['t0']), ((data['t6']/data['t0'])-1) , np.where(data['t6']<(0.97*data['t0']), ((data['t6']/data['t0'])-1), 
               np.where(data['t7']> (1.07*data['t0']), ((data['t7']/data['t0'])-1), ((data['t7']/data['t0'])-1))))))))))))))



data = data[data['t7'].notnull()]

del df_staging

# %%
## Call shortlisted stock
tasks_shortlisted = table_service.query_entities('dailyscorednew')
df_shortlisted = pd.DataFrame(tasks_shortlisted)


data = data[data['name'].isin(df_shortlisted['name'].to_list())]
data



# %%
index_var = ['name', 'date_rv1']
scenario_var = ['target_d3_p3', 'target_d3_p5',	'target_d3_p7', 'target_d5_p3', 'target_d5_p5', 'target_d5_p7', 'target_d7_p3', 'target_d7_p5', 'target_d7_p7']
scenario_var_price = ['target_price_d3_p3', 'target_price_d3_p5',	'target_price_d3_p7', 'target_price_d5_p3', 'target_price_d5_p5', 'target_price_d5_p7', 
                      'target_price_d7_p3', 'target_price_d7_p5', 'target_price_d7_p7']
price_var = ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']


df_result = data[index_var + scenario_var]

df_hit = pd.melt(df_result, id_vars=index_var, value_vars=scenario_var, var_name='scenario_check', value_name='hit')
df_hit['scenario'] = df_hit['scenario_check'].str.split('target_').str[1]

df_result = data[index_var + scenario_var_price]
df_per = pd.melt(df_result, id_vars=index_var, value_vars=scenario_var_price, var_name='scenario_check', value_name='perc')
df_per['scenario'] = df_per['scenario_check'].str.split('target_price_').str[1]

df_result = data[index_var + ['t0']]
df_price_base = pd.melt(df_result, id_vars=index_var, value_vars=['t0'], var_name='t0', value_name='t0_price')
df_price_base = df_price_base.drop_duplicates(subset=['name', 'date_rv1'], keep='first')
df_price_base

del df_result
del data


# %%
df_final = df_hit.merge(df_per, how='left', left_on=['name', 'date_rv1', 'scenario'], right_on =['name', 'date_rv1', 'scenario'])
del df_hit
del df_per

df_final = df_final[['name', 'date_rv1', 'hit', 'scenario', 'perc']]
df_final = df_final.merge(df_price_base, how='left', left_on=['name', 'date_rv1'], right_on =['name', 'date_rv1'])
del df_price_base


df_final = df_final[['name', 'date_rv1', 'hit', 'scenario', 'perc', 't0_price']]
df_final

df_final = df_final.rename(columns={"name": "tracking_name", "scenario": "tracking_scenario"})


# %%
df_shortlisted = df_shortlisted[['name', 'date', 'scenario', 'band']]
df_shortlisted


df_final_table = df_shortlisted.merge(df_final, how = 'left', left_on=['name', 'date', 'scenario'], right_on=['tracking_name', 'date_rv1', 'tracking_scenario'])
del df_final
del df_shortlisted

df_final_table = df_final_table[['name', 'date', 'band', 'scenario', 'hit', 't0_price', 'perc']]
df_final_table = df_final_table[df_final_table['perc'].notnull()]
df_final_table

date_today = datetime.today().strftime('%Y-%m-%d')
df_final_table['PartitionKey'] = date_today
df_final_table



# %%
## Call shortlisted stock
tasks_base = table_service.query_entities('resulttracking')
df_tracking_base = pd.DataFrame(tasks_base)
df_tracking_base = df_tracking_base[['name', 'date', 'band', 'scenario', 'hit', 't0_price', 'perc', 'PartitionKey']]

# %%
df_final_table_new = pd.concat([df_tracking_base, df_final_table], ignore_index=True) 

del df_tracking_base
del df_final_table

df_final_table_new = df_final_table_new.sort_values(by=['name', 'scenario', "PartitionKey"], ascending=True)
df_final_table_new



# %%
df_final_table_new = df_final_table_new.drop_duplicates(subset=['date', 'name', 'scenario'], keep=False)
df_final_table_new

# %%
##########################
# Write to Azure Table  ##
##########################

## Write to Azure Table

TOLOADINTOTABLE = "resulttracking"


def doLoad(ts):
    df = df_final_table_new.copy()
    df= df.to_dict('records')
    rows = [row for row in df]    
    for row in rows:
        a = row['PartitionKey']
        row['PartitionKey'] = a
        row['RowKey'] = row['name'] + row['date'] + row['scenario']
        ts.insert_or_replace_entity(TOLOADINTOTABLE, row)

table_service = TableService(connection_string=CONNECTION_STRING)
table_service.create_table(TOLOADINTOTABLE)
doLoad(table_service)

print ("Done load to Azure Table")


# %%



