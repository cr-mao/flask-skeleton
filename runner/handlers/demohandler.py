import logging

from .base_handler import api
from .base_handler import BaseHandler
from runner import app

logger = app.logger


class demoHandler(BaseHandler):

    @api({
        "type": "object",
        "properties": {
            "arg1": {
                "type": "string",
                "minLength": 9,
                "maxLength": 9,
            },
        },
        "required": ["arg1"]
    })
    def info(self):
        acc_types = self.payload.get('arg1') or 1
        logger.info("ddddkdkdk22222")
        return self.make_return(data=acc_types)
