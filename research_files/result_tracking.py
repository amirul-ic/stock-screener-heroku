## Merge with actual result

## Get list of shortlisted stocks

from azure.data.tables import TableClient
from azure.cosmosdb.table.tableservice import TableService
import pandas as pd
import numpy as np

CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockscreeneramirul;AccountKey=iMA+0QKbFkLtHQMoNzeHk/XAsqRLApK2Qi3T7hk52niWnJYKITy3YfoJ/TtBoiEi4oa4gfn4AUHw+ASt5zu/gQ==;EndpointSuffix=core.windows.net"
table_client = TableClient.from_connection_string(conn_str=CONNECTION_STRING, table_name='dailyscored')
table_service = TableService(connection_string=CONNECTION_STRING)


entities = table_service.query_entities('dailyscorednew')

df = pd.DataFrame(entities)
df = df[['id_scored', 'name', 'date', 'scenario']]


## Price result

entities = table_service.query_entities('sevendaysprice')
df_price = pd.DataFrame(entities)
df_price.rename(columns={'name': 'name_base'},inplace=True)
df_price = df_price.iloc[:,3:]


##Merge with price
df_master = df.merge(df_price[['date_base', 'name_base', 't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']], how='left', left_on=['name', 'date'], right_on=['name_base', 'date_base'] )
df_master = df_master.drop(columns=['name_base', 'date_base'])

del df

## Melt Data

index_var = ['name_base', 'date_base']
scenario_var = ['target_d3_p3', 'target_d3_p5',	'target_d3_p7', 'target_d5_p3', 'target_d5_p5', 'target_d5_p7', 'target_d7_p3', 'target_d7_p5', 'target_d7_p7']

df_result = df_price[index_var + scenario_var]

del df_price

df_result = pd.melt(df_result, id_vars=index_var, value_vars=scenario_var, var_name='scenario_check', value_name='succes')


df_master = df_master.merge(df_result, how='left', left_on=['name', 'date', 'scenario'], right_on = ['name_base', 'date_base', 'scenario_check'])
df_master = df_master.drop(columns = ['name_base', 'date_base', 'scenario_check'])
df_master['RowKey'] = df_master['id_scored'] + "_at_" + df_master['date']

###########################
## Write to Azure Table  ##
###########################

## Write to Azure Table

TOLOADINTOTABLE = "resulttracking"

def doLoad(ts):
    df = df_master.copy()
    df['PartitionKey'] = df['date']
    df= df.to_dict('records')
    rows = [row for row in df]    
    for row in rows:
        a = row['PartitionKey']
        row['PartitionKey'] = a
        ts.insert_or_replace_entity(TOLOADINTOTABLE, row)

table_service = TableService(connection_string=CONNECTION_STRING)
table_service.create_table(TOLOADINTOTABLE)
doLoad(table_service)

print ("Done load to Azure Table")