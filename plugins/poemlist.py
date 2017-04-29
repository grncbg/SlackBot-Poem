# coding: utf-8
""" ポエムを読み込む """

import pandas

class Poem:
    """ ポエムを取得するクラス """
    def __init__(self, dir):
        self.csv = dir

    def read_from_csv(self, path):
        """ ポエムをCSVから読み込む """
        self.csv = pandas.read_csv(path)

    def get_poems(self):
        """ ポエムを返す """
        return self.csv
