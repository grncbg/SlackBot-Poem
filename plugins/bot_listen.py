# coding: utf-8
""" channelへ発言が来た時 """
from slackbot.bot import listen_to
import poemlist
import select_random

DIR = "../poem/poem.csv"

@listen_to("ポエム")
def random_poem(message):
    """ ランダムにポエムを返す """
    poem = poemlist.Poem(DIR)
    poems = poem.get_poems()
    random = select_random.SelectRandom(poems)
    print(random)
