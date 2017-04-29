# coding: utf-8
""" ポエムを読み込む """

import pandas

class Poem:
    """ ポエムを取得するクラス """
    def __init__(self, path):
        self.csv = pandas.read_csv(path)

    def get_poems(self):
        """ ポエムを返す """
        return self.csv
