# -*- coding: utf-8 -*-
import threading


class BaseService(object):
    """
    基础服务类，是单例。

    类的生命周期为第一次获取实例初始化后永不销毁，除非显式移除

    后面考虑根据Flask的请求周期进行销毁工作
    """

    _instances = {}

    @classmethod
    def get_instance(cls):
        with threading.Lock():
            name = cls.__module__ + '.' + cls.__name__
            if name not in BaseService._instances:
                rv = cls()
                BaseService._instances[name] = rv
            else:
                rv = BaseService._instances[name]
        return rv
