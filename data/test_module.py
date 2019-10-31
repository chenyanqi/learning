from connect import  session
from user_module import User

def add_user():
    person = User(name='chenyanqi',password='qwe123')
    #session.add(person)
    session.add_all(
        [User(name='shuaiqi',password='123'),
        User(name='shuaiqishuaiqi',password='123')]
    )
    session.commit()  #提交

def search_user():
    rows = session.query(User).all()
    print(rows)

def update_user():
    row = session.query(User).filter(User.name=='chenyanqi').update({User.password:123456})
    session.commit()


def delete_user():
    row = session.query(User).filter(User.name == 'chenyanqi')[0]
    print(row)
    session.delete(row)
    session.commit()
if __name__ == '__main__':
    #add_user()  #一定要调用函数
    #update_user()
    #delete_user()
    search_user()

