import requests
import json
import pandas as pd
import sqlite3

# CONSTANTS
API_URL = 'https://kartta.hel.fi/ws/geoserver/avoindata/wfs'
db_col_names = [ 'north_coordinate', 'east_coordinate', 'construction_date', 'floor_area', 'utility', 'zipcode']

def fetch_data_to_df(xml_request):

    ####################################################################
    ###  This function fetches the data from api to pandas dataframe ###
    ####################################################################

    # First we send the xml-post request to the api
    with open(xml_request, 'r') as x:
        r = requests.post(API_URL, data=x, headers={'Content-Type':'text/xml'})
    
    # Next the data is transformed from JSON to python dictionary to pandas dataframe
    try:
        data = json.loads( r.content.decode('utf-8') )['features']
        return pd.DataFrame([ x['properties'] for x in data ] ).set_index('id')
    except Exception as ex:
        print(f"Something failed when trying to transform json-data into dataframe with following error: \n\t {ex}")
        return pd.DataFrame({})

def push_df_to_db( df, db_name='reagle.db', table_name='reagle'):

    ####################################################################
    ###  This function inserts data from dataframe to local database ###
    ####################################################################

    # We make a connection to the local database
    # The sqlite3 library creates the database if it does not alreade exist
    with sqlite3.connect(f'databases/{db_name}') as conn:

        # The column names are changed
        df.columns=db_col_names

        # The time of day is removed from the datetime of construction
        df['construction_date'] = df['construction_date'].apply( lambda s: s.split('T')[0] if s else None )

        # Data is pushed to database using panda's built-in method 'to_sql'
        df.to_sql(table_name, conn)


def query_from_db( query = 'SELECT * FROM reagle', db_name='reagle.db' ):

    ###########################################################
    ###  This function queries data from the local database ###
    ###########################################################

    # The data is read using pandas built-in method 'read_sql_query'
    with sqlite3.connect(f'databases/{db_name}') as conn:
        return pd.read_sql_query(query,conn).set_index('id')

