# -*- coding: utf-8 -*-
"""
@author: maozy
@time: 2024/8/30 11:54
"""
from dotenv import load_dotenv
import os

env = "local"
is_dev = True

def loadEnv():
    # 加载.env环境变量
    load_dotenv()
    env = os.environ.get("ENV") if os.environ.get("ENV") else "local"
    is_dev = env == "local"
