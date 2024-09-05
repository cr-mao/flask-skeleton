from runner.db.db_util import transaction
from runner.services import BaseService
from runner.resource import R


class AccountService(BaseService):

    def consume_log_type_list(self):
        log_type_list = [{
            "log_type": -1,
            "type_name": "全部"
        }]
        with transaction(R.DbSession) as session:
            sql = """
                  select 1
                """
            res = session.execute(sql).fetchone()

            # insertsql = """
            #     insert into
            # """
            # session.execute(insertsql)
            print(res[0])
        return log_type_list
