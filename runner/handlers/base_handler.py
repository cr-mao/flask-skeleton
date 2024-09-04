import logging

from flask import request
from flask.json import jsonify
from flask.views import View
from jsonschema import ValidationError, validate
from werkzeug.exceptions import HTTPException, NotFound

from runner import codes
from runner.confs import is_dev


def api(schema=None, need_login=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            if schema:
                try:
                    validate(self.payload, schema)
                except ValidationError as e:
                    logging.warning('ValidationError of %s: %s', request.path, e.message)
                    if is_dev:
                        return self.make_return(codes.INVALID_INPUT, msg=e.message)
                    else:
                        return self.make_return(codes.INVALID_INPUT)
            # 需要登录的，这里处理
            if need_login:
                return self.make_return(codes.NOT_LOGIN)

            return func(*args, **kwargs)

        wrapper.is_api = True  # BaseHandler根据is_api判断一个函数是普通函数还是API函数
        return wrapper

    return decorator


def check_token(payload: dict):
    auth_token = request.cookies.get('token')

    return True


# 所有处理器都继承这个 基础处理器
class BaseHandler(View):
    methods = ['POST']

    def log_error(self, error_code, http_code, data):
        payload = getattr(self, "payload", "-")
        log_msg = 'err_code: %s path: %s\n payload: %s, return: %s'
        logging.warning(log_msg, error_code, request.path, payload, data)

    # 错误返回
    def make_return(self, error_code: int = 0, msg: str = 'success', data: dict = None, http_code: int = 200):
        if error_code != 0 or http_code != 200:
            self.log_error(error_code, http_code, data)

        ret = {
            'error_code': error_code,
            'data': data,
            'msg': msg
        }
        return ret, http_code

    def dispatch_request(self, *args, **kwargs):

        try:
            try:
                payload = request.get_json(force=True)
            except Exception:
                payload = {}
            self.payload = payload or {}

            logging.debug('request payload: %s', payload)
            action = kwargs.pop('action')
            assert action is not None, "no action in url"
            meth = getattr(self, action, None)
            if meth is not None and getattr(meth, 'is_api', False) is True:
                logging.debug(f'activating {meth}')
            else:
                logging.error('unimplemented action %s', action)
                raise NotFound
            rs_data, http_code = meth()
            assert isinstance(rs_data, dict)
            return jsonify(rs_data)
        except AssertionError:
            logging.warning('wrong input', exc_info=True)
            http_code = 422
            return self.make_return(codes.INVALID_INPUT, http_code=http_code)
        except HTTPException as e:
            logging.warning('http exception error', exc_info=True)
            return self.make_return(http_code=e.code)
        except Exception:
            logging.exception('unknown error', exc_info=True)
            http_code = 500
            return self.make_return(codes.INNER_ERROR, http_code=http_code)
        finally:
            pass
