# -*- coding: utf-8 -*-
import psycopg2
import time
import pandas as pd
def work_time(st_time):
    '''Calculating working time in minutes. start_time = time.time() on input'''
    return round((time.time()-st_time)/60, 3)

class db():
    def __init__(self, connect_info):
        '''Init should be done from dict with keys: database, user, password, host, port
        Example: {"database":"public", "user":"admin", "password":"admin","host":"127.0.0.0","port":"5432"}
        '''
        self.user = connect_info['user']
        self.password = connect_info['password']
        self.host = connect_info['host']
        self.database = connect_info['database']
        if 'port' in connect_info:
            self.port = connect_info['port']

    def create_connection(self):
        try:
            if hasattr(self, 'port'):
                return psycopg2.connect(user = self.user, password = self.password, host = self.host, database = self.database, port = self.port)
            else:
                return psycopg2.connect(user = self.user, password = self.password, host = self.host, database = self.database)
        except:
            return psycopg2.connect(user = self.user, password = self.password, host = self.host)

    def execute(self, request, commit = True):
        try:
            start_time = time.time()
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(request)
            if commit:
                conn.commit()
            cursor.close()
            conn.close()
            return {'result_code': 1, 'error':'', 'time': work_time(start_time), 'request':request}
        except Exception as e:
            return {'result_code': 0, 'error': str(e), 'time': work_time(start_time), 'request':request}
    
    def check_connection(self):
        exe = self.execute(request = 'select 1')
        return True if exe['result_code'] == 1 else False
    
    def load_data_to_pandas(self, request):
        try:
            start_time = time.time()
            conn = self.create_connection()
            df = pd.read_sql_query(request, conn)
            conn.close()
            return {'result_code': 1, 'error':'', 'time': work_time(start_time), 'request':request, 'result':df}
        except Exception as e:
            return {'result_code': 0, 'error': str(e), 'time': work_time(start_time), 'request':request, 'result':None}
    
    def create_table(self, table_name, col_set, type_set):
        try:
            start_time = time.time()
            req = 'create table {} '.format(table_name)
            req_arr = []
            for col, dtype in zip(col_set,type_set):
                req_arr.append('{} {}'.format(col, dtype))
            req += '({})'.format(','.join(req_arr))
            exe = self.execute(request = req)
            return {'result_code': exe['result_code'], 'error':exe['error'], 'time': work_time(start_time), 'request':exe['request']}
        except Exception as e:
            return {'result_code': 0, 'error': str(e), 'time': work_time(start_time), 'request':None, 'result':None}

    def get_max_value(self, table_name, column_name):
        try:
            start_time = time.time()
            req = 'select max({0}) as {0} from {1}'.format(column_name, table_name)
            exe = self.load_data_to_pandas(req)
            return {'result_code': exe['result_code'], 'error':exe['error'], 'time': work_time(start_time), 'request':exe['request'], 'result':exe['result'][column_name].values[0]}
        except Exception as e:
            return {'result_code': 0, 'error': str(e), 'time': work_time(start_time), 'request':None, 'result':None}

    def update_value(self,table_name, column, condition, new_value):
        try:
            start_time = time.time()
            req = 'UPDATE {table_name} SET {column} = {new_value} WHERE {condition}'.format(table_name = table_name
                                                                                    , column = column
                                                                                    , new_value = new_value
                                                                                    , condition=condition)            
            exe = self.execute(request = req)
            return {'result_code': exe['result_code'], 'error':exe['error'], 'time': work_time(start_time), 'request':exe['request']}
        except Exception as e:
            return {'result_code': 0, 'error': str(e), 'time': work_time(start_time), 'request':None, 'result':None}
    
    #def insert_one_row():
    #    pass TODO