# -*- coding: utf-8 -*-
from runner import app

if __name__ == '__main__':
    # 资源初始化，如logger，db等
    app.ready()
    app.logger.info("this a script job")
