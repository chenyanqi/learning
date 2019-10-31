from sqlalchemy import  create_engine


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'learn'
USERNAME = 'admin'
PASSWORD = 'Root110qwe'


Db_uri = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(Db_uri)

from sqlalchemy.ext.declarative import  declarative_base
Base = declarative_base(engine)

if __name__ == '__main__':
    conection = engine.connect()
    result = conection.execute('select 1')
    print(result.fetchone())


