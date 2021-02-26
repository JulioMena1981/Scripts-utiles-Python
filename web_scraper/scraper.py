#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = input('Insert URL: ')

request = requests.get(url).text
parse = BeautifulSoup(request, 'html.parser')
search = parse.find_all('a')

for links in search:
    print(links.get('href')) 