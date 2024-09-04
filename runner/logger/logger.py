import logging
import json
from logging.handlers import RotatingFileHandler


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
            'args': record.args,
        }
        return json.dumps(log_record)


def set_logger(level="INFO", log_file="logs/app.log"):
    logger = logging.getLogger()
    log_level = getattr(logging, level)
    logger.setLevel(log_level)  # 这里只能限制直接通过root logger写的日志等级，所以后面handler还要再次限制level
    formatter = JsonFormatter()
    # 添加控制台处理程序
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 添加滚动文件处理程序
    file_handler = RotatingFileHandler(log_file, maxBytes=50000000, backupCount=5)  # 每个文件最大50mb 最多保留5个文件
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 将 Werkzeug 日志级别设置为 CRITICAL，以关闭日志记录
    # logging.getLogger('werkzeug').setLevel(logging.CRITICAL)
    return logger
