from .base_handler import api
from .base_handler import BaseHandler
from runner import app
from runner.services.account_service import AccountService

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
        logger.info(acc_types)
        data = AccountService.get_instance().consume_log_type_list()
        logger.info("this a demo log print")
        return self.make_return(data=data)
