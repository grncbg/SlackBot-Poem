# coding: utf-8
""" botの実行 """

from slackbot.bot import Bot
from crontab import CronTab
import scheduled_poem

def main():
    """ main 関数 """
    bot = Bot()

    bot.run()

if __name__ == "__main__":
    main()
