import sys
import requests
from english_words import english_words_set
from bs4 import BeautifulSoup
import json

BASE = "http://127.0.0.1:5000/"



response = requests.get(BASE + "webpage/yes")
print(response.json())
