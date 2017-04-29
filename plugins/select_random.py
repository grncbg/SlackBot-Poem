# coding: utf-8
""" ポエムをランダムに選択する """

import random

class SelectRandom:
    """ ポエムをランダムに選択する """
    def __init__(self, poem):
        self.poem = poem

    def get_random_poem(self):
        """ ランダムなポエムを返す """
        num = len(self.poem)
        rand = random.randint(0, num)
        name = self.poem["name"][rand]
        poem = self.poem["poem"][rand]
        return {"name":name, "poem":poem}
