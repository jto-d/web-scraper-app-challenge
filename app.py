from flask import Flask, render_template
import requests
from english_words import english_words_set
from bs4 import BeautifulSoup
import json
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo.html')


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
            if not word[-1].isalpha():
                word=word[:-1]
            if word in words_and_frequencies:
                words_and_frequencies[word] += 1
            elif word in english_words_set:
                words_and_frequencies[word] = 1 

    for word_check in most_common_words:
        if word_check in words_and_frequencies.keys():
            words_and_frequencies.pop(word_check)

    return words_and_frequencies


@app.route('/<name>/')
def my_view_func(name):
    return name

@app.route('/webpage/<url>/')
def get_words(url):
    url = urllib.parse.unquote(str(url))
    return scrape(url)
    

@app.route('/twitter')
def get_tweets():
    return {"words":1}

if __name__=='__main__':
    app.debug = True
    app.run()