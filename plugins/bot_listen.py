# coding: utf-8
""" channelへ発言が来た時 """

from slackbot.bot import listen_to
from slacker import Slacker
import slackbot_settings
from . import poemlist
from . import select_random

DIR = "poem/poem.csv"

@listen_to("ポエム")
def rondom_poem(message):
    """ ランダムにポエムを返す """
    slack = Slacker(slackbot_settings.API_TOKEN)
    poem = poemlist.Poem(DIR)
    poems = poem.get_poems()
    random = select_random.SelectRandom(poems)
    name, poem = random.get_random_poem()
    slack.chat.post_message(
        "bot-test",
        poem+" by @"+name,
        username=name,
        icon_emoji=":"+name+":",
        link_names=True
        )
