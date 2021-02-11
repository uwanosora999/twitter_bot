# -*- coding: utf-8 -*-
import requests
import linecache
import tweepy
import os

def tweet():
    #from requests_oauthlib import OAuth1Session
    CK=os.environ["CONSUMER_KEY"]
    CS=os.environ["CONSUMER_SECRET"]
    AT=os.environ["ACCESS_TOKEN_KEY"]
    AS=os.environ["ACCESS_TOKEN_SECRET"]
    AUTH=os.environ["AUTHOR"]

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    status = api.user_timeline(id=AUTH,count = 5)

    for mention in status:
        if '@' in mention.text:
            pass
        else:
            reply_text = "@"+str(mention.user.screen_name)+" "+"呼吸できて偉い"
            api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
            api.create_favorite(mention.id)

def reply():
    CK=os.environ["CONSUMER_KEY"]
    CS=os.environ["CONSUMER_SECRET"]
    AT=os.environ["ACCESS_TOKEN_KEY"]
    AS=os.environ["ACCESS_TOKEN_SECRET"]
    AUTH=os.environ["AUTHOR"]

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    status = api.mentions_timeline(count = 10) 
    for mention in status:
        if mention.user.screen_name == AUTH:
            reply_text = "@"+str(mention.user.screen_name)+" "+"リプライできて偉い"
        else:
            reply_text = "@"+str(mention.user.screen_name)+" "+"リプライなんて誰でもできる"
        api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
        api.create_favorite(mention.id)


if __name__ == "__main__":
    tweet()
    #reply()