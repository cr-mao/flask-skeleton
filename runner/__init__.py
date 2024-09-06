# -*- coding: utf-8 -*-
"""
@author: maozy
@time: 2024/8/30 11:52
"""
import os
import sys
from flask import Flask
from runner.confs import is_dev, log_level
from runner.resource import R

RUNNER_ROOT = os.path.abspath(os.path.dirname(__file__))


# 框架应用
class AppLication(object):

    def __init__(self):
        self.flaskApp = Flask(__name__)
        sys.path.append(os.path.dirname(RUNNER_ROOT))

    def ready(self, **kwargs):
        """
        资源初始化
        :param kwargs:
        :return:
        """

        from runner.logger.logger import set_logger
        # 单例 ，请使用这个logger
        self.logger = set_logger(log_level)
        # 初始化一些全局使用的资源
        R.initial()

    def setRoute(self):
        """
        路由注册
        :return:
        """
        from runner.routes.game_route import game_bp
        # 注册蓝图
        self.flaskApp.register_blueprint(game_bp)

        # 开发环境下设置跨域
        # if is_dev:
        @self.flaskApp.after_request
        def set_cors(resp):
            resp.headers["Access-Control-Allow-Origin"] = "*"
            resp.headers["Access-Control-Allow-Methods"] = "HEAD,OPTIONS,GET,POST,PUT,DELETE"
            resp.headers[
                "Access-Control-Allow-Headers"] = "Content-Type,Server,Date,Content-Length,Cache-Control,Keep-Alive,Connection,X-Requested-With,X-File-Name,Origin,Accept"
            resp.headers["Access-Control-Max-Age"] = "1728000"
            return resp

    def run(self):
        """
        启动 是给api 服务用的。 这里会注册路由
        :return:
        """
        self.setRoute()
        if (os.environ.get("ENV") == "local"):
            app.flaskApp.run('0.0.0.0', 5000, threaded=True, debug=False)
        else:
            app.flaskApp.run('0.0.0.0', 5000, threaded=True, debug=False)


app = AppLication()
