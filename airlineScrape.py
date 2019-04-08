import requests
import os
import time
import datetime
from selenium import webdriver


if not os.path.exists("chs-nyc_html"):
	os.mkdir("chs-nyc_html")

browser = webdriver.Chrome()

url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:chs,to:nyc,departure:04/16/2019TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

browser.get(url)

time.sleep(5)

innerHTML = browser.execute_script("return document.body.innerHTML")

outputFile = open("chs-nyc_html/seleniumScrape.html", "w")

outputFile.write(innerHTML) 