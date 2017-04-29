# coding: utf-8
""" channelへ発言が来た時 """
from slackbot.bot import listen_to

@listen_to("あきらめたら")
@listen_to("諦めたら")
def anzai(message):
    """ 諦めたらそこで試合終了ですよ """
    message.send("そこで試合終了ですよ。")

@listen_to("いいですか")
def reaction(message):
    """ リアクション """
    message.react("+1")
