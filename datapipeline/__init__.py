from .api import fetch_data_to_df, push_df_to_db, query_from_db, db_col_names

MAIN_REQUEST = 'datapipeline/requests/fetch_all_data.xml'

def init_database():
    df = fetch_data_to_df(xml_request=MAIN_REQUEST)
    push_df_to_db(df)