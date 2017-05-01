# coding: utf-8
""" botの実行 """

from slackbot.bot import Bot
from multiprocessing import Pool
from crontab import CronTab
import scheduled_poem

def main():
    """ main 関数 """
    bot = Bot()

    jobConfigs = [
        scheduled_poem.JobConfig(CronTab("00 0 * * *"), scheduled_poem.job1)
    ]

    # 処理を並列に実行
    p = Pool(len(jobConfigs))

    bot.run()
    p.map(scheduled_poem.job_controller, jobConfigs)

if __name__ == "__main__":
    main()
