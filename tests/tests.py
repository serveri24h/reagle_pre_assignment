import os,sys
sys.path.insert(0, os.getcwd())
from datapipeline import fetch_data_to_df, push_df_to_db, query_from_db, db_col_names

TEST_REQUEST = 'datapipeline/requests/fetch_test_data.xml'

def testmodule0():
    # test's database connection
    try:
        df = fetch_data_to_df(xml_request=TEST_REQUEST)
        assert df.columns.to_list() == ['i_nkoord', 'i_ekoord', 'c_valmpvm', 'i_kerrosala', 'c_kayttark', 'postinumero'], "Columns did not match"
    except Exception as e:
        print(f"testmodule failed when obtaining data an error: \n\t {e}" )
        return -1
    try:
        push_df_to_db(df, db_name='test.db', table_name='test')
    except Exception as e:
        print(f"testmodule-0 failed when pushing data to database with an error: \n\t {e}" )
        return -1
    return 0

def testmodule1():
    # test querying data from database
    try:
        df = query_from_db(db_name='test.db', query='SELECT * FROM test')
        assert df.columns.to_list() == db_col_names, "Columns did not match"
        return 0
    except Exception as e:
        print(f"testmodule-1 failed when trying to query data from local database with an error: \n\t {e}" )
        return -1



if __name__=='__main__':
    
    # CLEAR OLD TEST DATABASE
    os.system('if [ -f databases/test.db ]; then rm databases/test.db; fi')

    # RUN TEST MODULES
    tests = [testmodule0, testmodule1]
    for i,t in enumerate(tests):
        if t() == 0:
            print(f"Testmodule-{i} succeeded!")
        else:
            print(f"Testmodule-{i} Failed! Exiting test-module...")
            break
