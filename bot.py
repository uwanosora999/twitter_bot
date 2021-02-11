# -*- coding: utf-8 -*-
import requests
import linecache
import tweepy
import os

def puttweet():
    #from requests_oauthlib import OAuth1Session
    CK=os.environ["CONSUMER_KEY"]
    CS=os.environ["CONSUMER_SECRET"]
    AT=os.environ["ACCESS_TOKEN_KEY"]
    AS=os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    status = api.user_timeline(id='uwanosora999',count = 5)

    for mention in status:
        reply_text = "@"+str(mention.user.screen_name)+" "+"呼吸できて偉い"
        api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
        api.create_favorite(mention.id)

    status = api.mentions_timeline(count = 5)

    for mention in status:
        reply_text = "@"+str(mention.user.screen_name)+" "+"リプライできて偉い"
        api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
        api.create_favorite(mention.id)





if __name__ == "__main__":
    puttweet()