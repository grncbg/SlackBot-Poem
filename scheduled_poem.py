# coding: utf-8
""" 定時実行 """

from slacker import Slacker
import slackbot_settings
from plugins import random_poem

DIR = "poem/poem.csv"

def main():
    """ ランダムにポエムを投げる """

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


if __name__ == "__main__":

    main()
