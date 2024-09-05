# -*- coding: utf-8 -*-
"""
@author: maozy
"""
from dotenv import load_dotenv
import os

load_dotenv()
env = os.environ.get("ENV") if os.environ.get("ENV") else "local"
is_dev = env == "local"
project_name = os.environ.get("PROJECT_NAME") if os.environ.get("PROJECT_NAME") else "project"
log_level = os.environ.get("LOG_LEVEL") if os.environ.get("LOG_LEVEL") else "DEBUG"


def get_db_url(config: dict) -> str:
    return 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
        config['user'],
        config.get('password'),
        config['host'],
        config['port'],
        config.get('db_name')
    )


DATABASE = {
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "user": os.environ.get("DB_USERNAME"),
    "password": os.environ.get("DB_PASSWORD"),
    "db_name": os.environ.get("DB_DATABASE"),
}
