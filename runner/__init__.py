# -*- coding: utf-8 -*-
"""
@author: maozy
@time: 2024/8/30 11:52
"""
import logging
import os
import sys
from flask import Flask
from runner.confs import is_dev
from runner.res import R

RUNNER_ROOT = os.path.abspath(os.path.dirname(__file__))


class AppLication(object):
    def __init__(self):
        self.flaskApp = Flask(__name__)
        sys.path.append(os.path.dirname(RUNNER_ROOT))

    def ready(self, **kwargs):
        """
        初始化 其他资源
        :param kwargs:
        :return:
        """
        from runner.logger.logger import set_logger
        # 单例 ，请使用这个logger
        self.logger = set_logger()
        # 初始化一些全局使用的资源
        R.initial()
        # 路由
        self.setRoute()

    def setRoute(self):
        from runner.routes.game_route import game_bp
        # 注册蓝图
        self.flaskApp.register_blueprint(game_bp)
        # 开发环境下设置跨域
        if is_dev:
            @self.flaskApp.after_request
            def set_cors(resp):
                resp.headers["Access-Control-Allow-Origin"] = "*"
                resp.headers["Access-Control-Allow-Methods"] = "HEAD,OPTIONS,GET,POST,PUT,DELETE"
                resp.headers[
                    "Access-Control-Allow-Headers"] = "Content-Type,Server,Date,Content-Length,Cache-Control,Keep-Alive,Connection,X-Requested-With,X-File-Name,Origin,Accept"
                resp.headers["Access-Control-Max-Age"] = "1728000"
                return resp

    def run(self):
        if (os.environ.get("ENV") == "local"):
            app.flaskApp.run('0.0.0.0', 5000, threaded=True, debug=False)
        else:
            app.flaskApp.run('0.0.0.0', 5000, threaded=True, debug=False)


app = AppLication()
