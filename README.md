# pgsql_connector
there is a some utilities based on psycopg2 package<br>
<h3>how to add</h3>

`pip install git+https://github.com/Ilwapoi/pgsql_connector`<br>
<h3>how to use</h3>

`connect_info_file_path: {"database":"public", "user":"admin", "password":"admin","host":"127.0.0.0","port":"5432"}`
```python
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
```
