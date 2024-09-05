from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from runner import confs
from runner.confs import get_db_url


def create_sessionmaker(db_config):
    db_url = get_db_url(db_config)
    engine = create_engine(db_url, pool_size=16, max_overflow=30,
                           pool_use_lifo=True, pool_pre_ping=True)
    session = sessionmaker(bind=engine, autocommit=False, expire_on_commit=False)
    print(session)
    return session


# 资源对象
class Resource:
    def __init__(self):
        self.DbSession = None

    def initial(self):
        # 数据库连接资源
        self.DbSession = create_sessionmaker(confs.ADB_DATABASE)


R = Resource()
