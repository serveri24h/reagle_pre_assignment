import requests
import json
import pandas as pd
import sqlite3

# CONSTANTS
API_URL = 'https://kartta.hel.fi/ws/geoserver/avoindata/wfs'
db_col_names = [ 'north_coordinate', 'east_coordinate', 'construction_date', 'floor_area', 'utility', 'zipcode']

def fetch_data_to_df(xml_request):
    with open(xml_request, 'r') as x:
        r = requests.post(API_URL, data=x, headers={'Content-Type':'text/xml'})
    try:
        data = json.loads( r.content.decode('utf-8') )['features']
        return pd.DataFrame([ x['properties'] for x in data ] ).set_index('id')
    except Exception as ex:
        print(f"Something failed when trying to transform json-data into dataframe with following error: \n\t {ex}")

def push_df_to_db( df, db_name='reagle.db', table_name='reagle'):
    with sqlite3.connect(f'databases/{db_name}') as conn:
        df.columns=db_col_names
        df['construction_date'] = df['construction_date'].apply( lambda s: s.split('T')[0] if s else None )
        df.to_sql(table_name, conn)


def query_from_db( query = 'SELECT * FROM reagle', db_name='reagle.db' ):
    with sqlite3.connect(f'databases/{db_name}') as conn:
        return pd.read_sql_query(query,conn).set_index('id')

