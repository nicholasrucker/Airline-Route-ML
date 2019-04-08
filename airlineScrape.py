import requests
import ssl
import os
import time
import datetime
from lxml import html

import re
import json
import urllib
import sys
import os
import logging

if not os.path.exists("html_files"):
	os.mkdir("html_files")


url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:chs,to:nyc,departure:04/16/2019TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
response = requests.get(url, headers=headers, verify=False)

outputFile = open("hopefullyworkTry2.html", "wb")

time.sleep(25)

outputFile.write(response.content)