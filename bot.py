# -*- coding: utf-8 -*-
import requests
import linecache
import tweepy
import os
import random
import json
import requests

### Twitter acount config ###
CK=os.environ["CONSUMER_KEY"]
CS=os.environ["CONSUMER_SECRET"]
AT=os.environ["ACCESS_TOKEN_KEY"]
AS=os.environ["ACCESS_TOKEN_SECRET"]
AUTH=os.environ["AUTHOR"]


def tweet():
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    status = api.user_timeline(id=AUTH,count = 1)

    ### Bot mention ###
    rep_sent = json.load(open("./sentence.json",'r')) 

    for mention in status:
        replies = tweepy.Cursor(api.search, q='to:{}'.format(AUTH),
                                since_id=mention.id, tweet_mode='extended').items()
        replies_name = [ tweet.user.screen_name for tweet in replies ]
        if not ( '@' in mention.text or api.me().screen_name in replies_name ):
            reply_text = "@"+str(mention.user.screen_name)+" "+random.choice(rep_sent['sentence'])
            api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
            api.create_favorite(mention.id)

def reply():
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    status = api.mentions_timeline(count = 5) 

    ### Bot mention ###
    for mention in status:
        replies = tweepy.Cursor(api.search, q='to:{}'.format(AUTH),
                                since_id=mention.id, tweet_mode='extended').items()
        replies_name = [ tweet.user.screen_name for tweet in replies ]

        if mention.user.screen_name == AUTH :
            reply_text = "@"+str(mention.user.screen_name)+" "+"リプライできて偉い"
        else:
            reply_text = "@"+str(mention.user.screen_name)+" "+"リプライなんて誰でもできる"

        if not ( api.me().screen_name in replies_name ):
            api.update_status(status = reply_text, in_reply_to_status_id = mention.id)
            api.create_favorite(mention.id)



if __name__ == "__main__":
    tweet()
    reply()