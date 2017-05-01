# coding: utf-8
""" ポエムをランダムに選択する """

from . import select_random
from . import poemlist

class RandomPoem:
    """ random poem """
    def __init__(self, path):
        self.path = path

    def get_random_poem(self):
        """ ランダムなポエムを返す """
        poem = poemlist.Poem(self.path)
        poems = poem.get_poems()
        random = select_random.SelectRandom(poems)
        return random.get_random_poem()
