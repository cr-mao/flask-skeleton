# -*- coding: utf-8 -*-
import hashlib


def md5sum(b):
    """
    获取二进制内容对应的md5散列值

    Args:
        :b: bytes

    Returns:
        str
    """
    if not isinstance(b, bytes):
        raise TypeError('b should be bytes')
    m = hashlib.md5()
    m.update(b)
    rv = m.hexdigest()
    return rv
