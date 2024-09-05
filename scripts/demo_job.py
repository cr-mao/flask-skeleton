from runner import R
from runner.logger.logger import set_logger

logger = set_logger()
# 资源初始化，db初始化
R.initial()

if __name__ == '__main__':
    logger.info("hello demo job")
