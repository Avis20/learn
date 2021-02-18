#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('home.html', **kwargs)


app.run(debug=True)

'''
import sys
import requests
from bs4 import BeautifulSoup as soup


def get_links(url):
    result = requests.get(url)
    html = result.text
    doc = soup(html)
    print(type(doc))
    links = []
    for el in doc.find_all('a'):
        links.append(el.get('href'))
    return links


if __name__ == '__main__':
    for url in sys.argv[1:]:
        print(url)
        for num, link in enumerate(get_links(url)):
            print(num, link)
'''

# import webbrowser

# url = 'https://python.org'
# webbrowser.open_new_tab(url)

# from flask import Flask, request, render_template

# app = Flask(__name__)


# @app.route('/echo/')
# def echo():
#     kwargs = {}
#     kwargs['param1'] = request.args.get('param1')
#     kwargs['param2'] = request.args.get('param2')
#     return render_template('flask2.html', **kwargs)


# if __name__ == '__main__':
#     app.run(port=9999, debug=True)

'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask.html', thing=thing)


app.run(port=9999, debug=True)
'''

'''
from bottle import route, run, static_file


@route('/')
def main():
    return static_file('index.html', root='.')


@route('/echo/<thing>')
def echo(thing):
    return "Hello %s\n" % thing

run(host='localhost', port=9999)
'''

'''
import requests
import json

url = 'http://api.quotable.io/random'
response = requests.get(url)
print(response)
# <Response [200]>

print(type(response.text))
print(response.text)
# <class 'str'>

data = json.loads(response.text)
print(data['content'])
# No one has ever become poor by giving.
'''

'''
import urllib.request as ur

url = 'http://api.quotable.io/random'
response = ur.urlopen(url)

for key, val in response.getheaders():
    print(key, '=', val)
'''

'''
import urllib.request as ur
import json

url = 'http://api.quotable.io/random'
response = ur.urlopen(url)
print(response)

json_str = response.read().decode('utf8')
data = json.loads(json_str)
print(data['content'])
'''
