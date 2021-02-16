#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/echo/<param1>/<param2>')
def echo(param1, param2):
    return render_template('flask2.html', param1=param1, param2=param2)


if __name__ == '__main__':
    app.run(port=9999, debug=True)

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
