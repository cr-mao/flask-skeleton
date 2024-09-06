# -*- coding: utf-8 -*-
from datetime import datetime

import simplejson


class MyJsonEncoder(simplejson.JSONEncoder):
    """
    根据实际使用情景，定制过的编码规则的编码器
    """

    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super().default(o)


# 全局的JSON编码器
# 默认配置
#   - Decimal 自动转为 float
#   - 键排序
#   - 不强制进行ASCII编码
#   - datetime 类型转为 %Y-%m-%d %H:%M:%S 字符串
json_encoder = MyJsonEncoder(
    use_decimal=True, ensure_ascii=False, sort_keys=True)


def json_encode(o):
    """
    使用全局JSON编码器进行JSON编码

    Returns:
        str
    """
    rv = json_encoder.encode(o)
    return rv


def json_decode(b):
    """
    将二进制内容解码为Python对象基础类型

    Returns:
        object
    """
    rv = simplejson.loads(b)
    return rv
