import sys
import requests
import nltk
import tweepy
from english_words import english_words_set
from bs4 import BeautifulSoup

consumer_key = "a4hSTEJnphYBtfFAVy2WwrEuj"
consumer_secret = "KdE8TZUdobZMR8eWfth3e6OvmUoCzwJjR3tX1XoYdH6OhsFb7R"
access_token = "1344016095632617475-TLiXlyr1pAZxfJMKoXqgamRJTlGLvl"
access_token_secret = "bCjLIjZ2Uk1bDj1QgxePBRo7GHKVOgndP6WYqc6b0o8hv"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
