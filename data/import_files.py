import csv
import sqlite3
from glob import glob

db_filename = 'db'
conn = sqlite3.connect(db_filename)

csv_files = glob('*.csv')

for csv_file in csv_files:
  table_name = csv_file[0:-4] # strip '.csv'
  print('processing ' + table_name)

  with open(csv_file, newline='') as fd:
    reader = csv.reader(fd)
    headers = reader.__next__()

    query = 'CREATE TABLE IF NOT EXISTS "' + table_name + '" ('
    for header in headers:
      query += '"' + header + '" TEXT, '
    query = query[0:-2] # strip the last ', '
    query += ')'

    #print(query)
    try:
      conn.execute(query)
    except Exception as e:
      print('query ' + query)
      raise e

    query = 'INSERT INTO ' + table_name + ' VALUES ('
    for column in headers:
      query += '?, '
    query = query[0:-2] # strip the last ', '
    query += ')'

    rows = []
    for row in reader:
      rows.append(row)

    try:
      conn.executemany(query, rows)
      conn.commit()
    except Exception as e:
      print('query ' + query)
      raise e
