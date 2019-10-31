from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from  data.connect import  Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)
    _locked = Column(Boolean,default=False,nullable=False)


if __name__ == 'main':
    Base.metadata.create_all()


