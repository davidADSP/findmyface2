
#!python3.5
#From https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-connect-query-python

import pyodbc

server = 'findmyface.database.windows.net'
database = 'FaceDB'
username = 'findmyface'
password = "Theyfinallyfedus!"
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Users;")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()
