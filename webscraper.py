#Python Webscraper

import sys
import requests

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


URL = "https://www.w3schools.com/python/python_file_open.asp"
page = requests.get(URL)


words_and_frequencies = {}

soup = BeautifulSoup(page.content, 'html.parser')
paragraph_text = soup.find_all("p")

for word in paragraph_text[0].text.strip().split():
  
  if not word.lower()[-1].isalpha():
    word=word[:-1]
  print(word)
  if word.lower() in english_words_set:
    print(word)
""" for p in paragraph_text:
  for word in p.text.strip().split():
    if word.lower() in words_and_frequencies:
      words_and_frequencies[word.lower()] += 1
    elif word.lower() in english_words_set:
      words_and_frequencies[word.lower()] = 1 """

""" words = list(words_and_frequencies.keys())
frequencies = list(words_and_frequencies.values())

print(words_and_frequencies)

textfile = open("words.txt", "w")
for element in words:
    textfile.write(element + "\n")
textfile.close()

textfile = open("frequencies.txt", "w")
for element in frequencies:
    textfile.write(str(element) + "\n")
textfile.close()

print("completed") """