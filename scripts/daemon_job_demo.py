# -*- coding: utf-8 -*-

from runner import app
from runner.common.job.daemon import DaemonJob


def run():
    job = AutoPostThumbTask()
    job.set_work_sleep(5)  # 运行时间间隔
    job.set_idle_sleep(5)  # 程序每次阻塞时间
    job.main()


class AutoPostThumbTask(DaemonJob):

    def work(self):
        app.logger.info("this as daemon job demo")


if __name__ == '__main__':
    app.ready()
    run()
