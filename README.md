# pgsql_connector
there is a some utilities based on psycopg2 package
how to add:  pip install git+https://github.com/Ilwapoi/pgsql_connector
how to use: 
import pgsql_connector
import json
with open(connect_info_file_path) as json_file:
    db_connect_info = json.load(json_file)
my_conn = pgsql_connector.db(connect_info = db_connect_info['my_account'])

script = 'select * from table'

exec_result = my_conn.load_data_to_pandas(script)

if exec_result['result'] == 1:
  df = exec_result['result']

else:
  print(exec_result['error'])
