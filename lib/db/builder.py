import sqlite3

def run_sqlfile(database_name, sql_file, file_type):
    conn = sqlite3.connect('bin/databases/' + str(database_name)) 
    c = conn.cursor()

    with open('./sql/' + file_type + '/' + sql_file, 'r') as content_file:
        c.execute(content_file.read())
    
    conn.commit()
    conn.close()

def run_sqlcode(database_name, sql_code):
    conn = sqlite3.connect('bin/databases/' + str(database_name)) 
    c = conn.cursor()
    c.execute(sql_code) 
    conn.commit()
    conn.close()

def print_table(database_name, table_name):
    conn = sqlite3.connect('bin/databases/' + str(database_name)) 
    c = conn.cursor()
    for row in c.execute('SELECT * FROM ' + table_name):
        print(row)
    conn.commit()
    conn.close()

def insert_into_table(database_name, table_name, values):
    values_count = '?,' * len(values)
    values_count = values_count[0:len(values_count) - 1]
    run_sqlcode(database_name, 'INSERT OR REPLACE INTO ' + table_name + ' VALUES (' + values_count + ')', values)