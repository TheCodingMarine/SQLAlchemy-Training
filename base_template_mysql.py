import os
from sqlalchemy import MetaData, create_engine

metadata = MetaData()


username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

engine = create_engine('mysql+pymysql://' + username + ':' + password + \
                        '@localhost/')
metadata.create_all(engine)