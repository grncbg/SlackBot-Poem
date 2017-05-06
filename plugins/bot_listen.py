# coding: utf-8
""" channelへ発言が来た時 """

from slackbot.bot import listen_to
from slacker import Slacker
import slackbot_settings
from . import random_poem

DIR = "poem/poem.csv"

@listen_to("ポエム")
@listen_to("ぽえむ")
@listen_to("poem")
def rondom_poem(message):
    """ ランダムにポエムを返す """
    slack = Slacker(slackbot_settings.API_TOKEN)
    random = random_poem.RandomPoem(DIR)
    name, poem = random.get_random_poem()
    slack.chat.post_message(
        message.body["channel"],
        poem+" by @"+name,
        username=name,
        icon_emoji=":"+name+":",
        link_names=True
        )
