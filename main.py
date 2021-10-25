from logging import debug
from flask import Flask, request
from flask_restful import Api, Resource
import sys
import requests
from english_words import english_words_set
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
api = Api(app)

words = {}

def remove_last_letter(w):
    try:
        if not w[-1].isalpha():
            w=w[:-1]
            w=remove_last_letter(w)
            return w
    except:
        return w

def scrape(URL) :
    
    page = requests.get(URL)

    filename = "common_words.txt"
    words_file = open(filename, 'r')
    most_common_words = [line.split('\n')[0] for line in words_file.readlines()]

    words_and_frequencies = {}

    soup = BeautifulSoup(page.content, 'html.parser')
    paragraph_text = soup.find_all("p")

    

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

    json_words = json.dumps(words_and_frequencies, indent=4)
    return json_words

class WebPage(Resource):
    def get(self, url):
        return scrape("https://www.w3schools.com/python/python_file_open.asp")







api.add_resource(WebPage, "/webpage/<string:url>")

if __name__=="__main__":
    app.run(debug=True)