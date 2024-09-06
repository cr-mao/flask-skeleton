# -*- coding: utf-8 -*-
import logging
import os
import signal
import time

from runner.common.job.abstract import AbstractJob

logger = logging.getLogger(__name__)


class DaemonJob(AbstractJob):

    def __init__(self):
        # 用来标记常驻运行标记
        self.running = False

        # 空闲时的休眠时间，秒
        self.idle_sleep = 3

        # 工作时的休眠时间，秒
        self.work_sleep = 0

        # 是否繁忙标记
        self.busy = False

        super().__init__()

    def prepare(self):
        self.running = True

        # 信号处理
        signal.signal(signal.SIGTERM, self.handle_signal)
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGQUIT, self.handle_signal)

    def main(self):
        self.prepare()
        self.loop()

    def set_work_sleep(self, i):
        """
        设置工作时的休眠时间
        """
        self.work_sleep = i

    def set_idle_sleep(self, i):
        """
        设置工作时的休眠时间
        """
        self.idle_sleep = i

    def set_busy(self, busy):
        """
        设置是否繁忙状态
        """
        self.busy = busy

    def loop(self):
        """
        主循环
        """
        while self.running:
            ok = False
            ts = time.time()
            try:
                self.pre_work_hook()
                ok = self.work()
                self.post_work_hook(ok)
                t = time.time() - ts
                if ok:
                    self.increase_ok(t)
                else:
                    self.increase_error(t)
            except Exception as e:
                self.handle_error(e)
                # 异常都算作失败
                t = time.time() - ts
                self.increase_error(t)

            if self.busy and self.work_sleep > 0:
                time.sleep(self.work_sleep)
            else:
                time.sleep(self.idle_sleep)

        logger.info('quit')

    def handle_error(self, ex):
        logger.warning('handling error, %s' % ex)
        raise ex

    def handle_signal(self, sig, frame):
        """
        默认的信号处理

        SIGTERM, 平滑处理好正在处理的后退出
        SIGINT, 平滑处理好正在处理的后退出
        SIGQUIT, 直接退出
        """
        if sig == signal.SIGTERM:
            logger.info('SIGTERM detected, graceful shutdown')
            self.running = False
        if sig == signal.SIGINT:
            logger.info('SIGINT detected, graceful shutdown')
            self.running = False
        if sig == signal.SIGQUIT:
            logger.info('SIGQUIT detected, bye!')
            os._exit(-1)

    def increase_ok(self, t, n=1):
        """
        用来作出处理成功后的操作，例如发送监控消息

        Args:
            :t: float 耗时
            :n: int 计数
        """
        pass

    def increase_error(self, t, n=1):
        """
        用来作出处理出错后的操作，例如发送监控消息

        Args:
            :t: float 耗时
            :n: int 计数
        """
        pass
