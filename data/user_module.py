from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime,Boolean

from  connect import  Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)
    _locked = Column(Boolean,default=False,nullable=False)

    def __repr__(self):
        return 'User(id=%s,name=%s,password=%s,creatime=%s,_locked=%s)' %(self.id,
                                                             self.name,
                                                             self.password,
                                                             self.creatime,
                                                             self._locked
                                                              )
if __name__ == '__main__':
    Base.metadata.create_all()


