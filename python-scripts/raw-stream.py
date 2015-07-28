# -*- coding: utf-8 -*-
import tweepy
import os
import json
import argparse

class EchoStreamListener(tweepy.StreamListener):
    def __init__(self, api ):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def on_data(self, tweet):
        tweet_data = json.loads(tweet)
        if 'text' in tweet_data:
            print tweet.rstrip()

    def on_error(self, status_code):
        return True

    def on_timeout(self):
        return True


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    sapi = tweepy.streaming.Stream(
        auth, EchoStreamListener( api=api ))
    sapi.sample()
