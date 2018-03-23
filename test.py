import tweepy
from textblob import TextBlob
import re


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())

consumer_key = 'hzWWIj8rAZIm8knatemXkbPpC'
consumer_secret = 'jbBTNbmEubICWRPEb3OH7bzpKiR5NQ5wM2BG3mE4a2WaBKVukg'

access_token = '977278387856330753-n7UJmE0SjF3G40L4M3N7AVFfF70hoTG'
access_token_secret = 'iZ3GLXcSB135VOnVwIdQVt1JFaY0K5VNLFCtbc7wQZrnS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    tweet_text = clean_tweet(tweet.text)
    analysis = TextBlob(clean_tweet(tweet))
