# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    userName = Column(String(20))
    passWord = Column(String(20))
    realName = Column(String(20))

# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/study')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).all()
for u in user:
    print('type:', type(u))
    print('userName:', u.userName)
    print('passWord:', u.passWord)
    print('realName:', u.realName)
# 打印类型和对象的name属性:
# print('type:', type(user))
# print('userName:', user.userName)
# print('passWord:', user.passWord)
# print('realName:', user.realName)
# 关闭session:
session.close()