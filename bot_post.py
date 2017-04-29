# coding: utf-8
""" botからの送信 """

from slacker import Slacker
import slackbot_settings

if __name__ == "__main__":
    SLACK = Slacker(slackbot_settings.API_TOKEN)
    SLACK.chat.post_message(
        "grade-2年生",
        "俺が神だ",
        username="uragou",
        icon_url="https://ca.slack-edge.com/T4RPCS75E-U4TBVEX6K-0510ae7df12f-512"
        )
