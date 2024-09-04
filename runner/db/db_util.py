from contextlib import contextmanager
from functools import wraps


@contextmanager
def transaction(Session):
    session = None
    try:
        session = Session()
        yield session
        session.commit()
    except Exception:
        if session:
            session.rollback()
        raise
    finally:
        if session:
            session.close()


def transaction_method(Session):
    """
        DB事务方法装饰器，会在原方法参数第一位注入session对象
    """

    def wrapper(func):
        @wraps(func)
        def wrapped(entity, *args, **kwargs):
            with transaction(Session) as session:
                return func(entity, session, *args, **kwargs)

        return wrapped

    return wrapper


# 事务注入
transaction_inject = transaction_method


def session_method(Conn):
    """
        事务方法装饰器，会在原方法参数第一位注入session对象
    """

    def wrapper(func):
        @wraps(func)
        def wrapped(entity, *args, **kwargs):
            return func(entity, Conn, *args, **kwargs)

        return wrapped

    return wrapper
