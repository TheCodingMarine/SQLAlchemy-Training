import os
from sqlalchemy import (MetaData, create_engine, Table, Column, Integer,
                        Numeric, String, ForeignKey, DateTime, null, 
                        ForeignKey, Boolean)
from datetime import datetime


metadata = MetaData()
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

#connect to the server and create a database 
mysql_engine = create_engine('mysql+pymysql://' + username + ':' + password + \
                        '@localhost/')
connection = mysql_engine.connect()
connection.execute("CREATE DATABASE <some_db_name>")
connection.execute("USE <some_db_name>")

# Create metadata here for tables.

# Create engine to connect to our database and persist the tables.
'<some_db_name>'_engine = create_engine('mysql+pymysql://' + username + ':' + password + \
                        '@localhost/<some_db_name>')
metadata.create_all('<some_db_name>'_engine)