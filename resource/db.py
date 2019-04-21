import pyodbc as db

server = 'mdpsqldbserverdev.database.windows.net'
database = 'mdpappdb'
username = 'mdpadmin'
password = 'Robo#2010'
port = 1433
driver = '{ODBC Driver 13 for SQL Server}'

connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'

connection = db.connect(connectionstring)
cursor = connection.cursor()