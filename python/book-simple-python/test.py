#!/usr/bin/env python3

import urllib.request as ur
import json

url = 'http://api.quotable.io/random'
response = ur.urlopen(url)
print(response)

json_str = response.read().decode('utf8')
data = json.loads(json_str)
print(data['content'])
