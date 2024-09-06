# -*- coding: utf-8 -*-
from runner.common.job.abstract import AbstractJob


class StandardJob(AbstractJob):
    """
    标准的一次性运行job
    """

    def main(self):
        self.prepare()
        try:
            self.pre_work_hook()
            _ = self.work()
            self.post_work_hook(_)
        except Exception as e:
            self.handle_error(e)
