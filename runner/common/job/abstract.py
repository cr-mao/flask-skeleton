# -*- coding: utf-8 -*-


class AbstractJob(object):

    def __init__(self):
        pass

    def prepare(self):
        """
        准备工作写在这个方法里
        """
        pass

    def main(self):
        """
        job入口、启动方法
        """
        raise NotImplementedError()

    def work(self):
        """
        主要用来做事的方法
        """
        raise NotImplementedError()

    def handle_error(self, ex):
        """
        错误处理
        """
        raise ex

    def pre_work_hook(self):
        """
        工作方法前置处理钩子
        """

    def post_work_hook(self, work_rv):
        """
        工作方法后置处理钩子
        """
