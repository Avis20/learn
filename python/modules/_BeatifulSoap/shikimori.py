import logging

import requests as r
from bs4 import BeautifulSoup as soup
from pprint import pprint

import http.client as http_client

http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

URL = "https://shikimori.one"
PATH = "catalog/item/drakon-gornichnaya-gospozhi-kobayashi-2"

response = r.get(f"{URL}/{PATH}", headers={
    'accept': "*/*",
    'User-Agent': 'Mozilla/5.0',
})
print(response)

