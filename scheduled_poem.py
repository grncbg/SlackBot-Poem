# coding: utf-8
""" 定時実行 """

from crontab import CronTab
from datetime import datetime, timedelta
from slackbot.bot import listen_to
from slacker import Slacker
import math
import time
import slackbot_settings
from plugins import random_poem

DIR = "poem/poem.csv"

class JobConfig(object):
    """　処理設定　"""

    def __init__(self, crontab, job):
        """
        :type crontab: crontab.CronTab
        :param crontab: 実行時間設定
        :type job: function
        :param job: 実行する関数
        """

        self._crontab = crontab
        self.job = job


    def schedule(self):
        """
        次回実行日時を取得する。
        :rtype: datetime.datetime
        :return: 次回実行日時を
        """

        crontab = self._crontab
        return datetime.now() + timedelta(seconds=math.ceil(crontab.next()))

    def next(self):
        """
        次回実行時刻まで待機する時間を取得する。
        :rtype: long
        :retuen: 待機時間(秒)
        """

        crontab = self._crontab
        return math.ceil(crontab.next())


def job_controller(jobConfig):
    """ 
    処理コントローラ
    :type crontab: crontab.CronTab
    :param crontab: 実行設定
    """

    while True:
        try:

            # 次実行時刻まで待機
            time.sleep(jobConfig.next())

            # 処理を実行する。
            jobConfig.job()
            
        except KeyboardInterrupt:
            break


def job1():
    """ ランダムにポエムを返す """
    slack = Slacker(slackbot_settings.API_TOKEN)
    random = random_poem.RandomPoem(DIR)
    name, poem = random.get_random_poem()
    slack.chat.post_message(
        "ポエム",
        poem+" by @"+name,
        username=name,
        icon_emoji=":"+name+":",
        link_names=True
        )

def main():
    """
    """

    # 毎分実行設定
    jobConfigs = [
        JobConfig(CronTab("00 0 * * *"), job1)
    ]

    # 処理を並列に実行
    p = Pool(len(jobConfigs))
    p.map(job_controller, jobConfigs)

