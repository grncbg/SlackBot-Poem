# coding: utf-8
""" botの実行 """

from slackbot.bot import Bot

def main():
    """ main 関数 """
    bot = Bot()

    bot.run()

if __name__ == "__main__":
    main()
