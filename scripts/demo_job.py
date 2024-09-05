from runner import R
from runner.logger.logger import set_logger
from runner.confs import log_level

print(log_level)
logger = set_logger(log_level)
# 资源初始化，db初始化
R.initial()

if __name__ == '__main__':
    logger.info("hello demo job")
