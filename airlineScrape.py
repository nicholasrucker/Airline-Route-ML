import requests
import os
import time
import datetime
from selenium import webdriver

# This will check to see if there is a directory for the flight data HTML
# If there is not one, one will be made
if not os.path.exists("chs-destination_html"):
	os.mkdir("chs-destination_html")


# Here we are declaring our web browser as Chrome
# This can be any browser you have installed on your computer that works with selenium
browser = webdriver.Chrome()

# Temp URL with no real destination
url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:chs,to:nyc,departure:04/16/2019TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.php"

# This command uses selenium to open a browser to truly act like a deveoper 
# It makes it so you can scrape webpages loaded by javaScript / have a lot of scraping preventions
browser.get(url)

# Lets sleep for a little bit after requesting the URL so all the JS can execute and we can get all the results
time.sleep(10)

# The script is executed which gets all the HTML from the website, even the part executed in JS
innerHTML = browser.execute_script("return document.body.innerHTML")

# A file is created with the destination city in the file name and the HTML is written to it
# You write to the file with just 'w' instead of 'wb' because the htlm is of type 'string' and not 'byte'
outputFile = open("chs-destination_html/<chs-desination2>.html", "w")
outputFile.write(innerHTML)

#decision tree or multiclass

#look at preprocessing