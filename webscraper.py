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


URL = "https://www.w3schools.com/python/python_file_open.asp"
page = requests.get(URL)

filename = "common_words.txt"
words_file = open(filename, 'r')
most_common_words = [line.split('\n')[0] for line in words_file.readlines()]

words_and_frequencies = {}

soup = BeautifulSoup(page.content, 'html.parser')
paragraph_text = soup.find_all("p")

def remove_last_letter(w):
  try:
    if not w[-1].isalpha():
      w=w[:-1]
      w=remove_last_letter(w)
    return w
  except:
    return w

for line in paragraph_text:
  for word in line.text.strip().split():
    word=word.lower()
    word = remove_last_letter(word)
    if word in words_and_frequencies:
      words_and_frequencies[word] += 1
    elif word in english_words_set:
      words_and_frequencies[word] = 1

for word_check in most_common_words:
  if word_check in words_and_frequencies.keys():
    words_and_frequencies.pop(word_check)


words = list(words_and_frequencies.keys())
frequencies = list(words_and_frequencies.values())
print(words)
print(frequencies)



textfile = open("words.txt", "w")
for element in words:
    textfile.write(element + "\n")
textfile.close()
textfile = open("frequencies.txt", "w")
for element in frequencies:
    textfile.write(str(element) + "\n")
textfile.close()
print("completed")


