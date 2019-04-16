import requests
import os
import time
import datetime
from selenium import webdriver

# This will check to see if there is a directory for the flight data HTML
# If there is not one, one will be made
if not os.path.exists("flightHtml"):
	os.mkdir("flightHtml")

# Here we are declaring our web browser as Chrome
# This can be any browser you have installed on your computer 
#		that works with selenium (eg. chrome, firefox, safari, etc...)
browser = webdriver.Chrome()

# This input file has all the airports of interest
# So we are just going to loop through the text file
inputFile = open("airports.txt", "r")
airports = inputFile.readlines()

for airport in airports:

	# Temp URL with no real destination
	url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:chs,to:" + airport + ",departure:05/20/2019TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.php"

	# This command uses selenium to open a browser to act like a deveoper 
	# It makes it so you can scrape webpages loaded by javaScript / have a lot of scraping preventions
	# It is also a little harder to get banned
	browser.get(url)

	# Lets sleep for a little bit after requesting the URL 
	#	Mainly so all the JS can execute and we can get all the results
	time.sleep(10)

	# The script is executed which gets all the HTML from the website, even the part executed in JS
	innerHTML = browser.execute_script("return document.body.innerHTML")

	# A file is created with the destination city in the file name and the HTML is written to it
	# You write to the file with just 'w' instead of 'wb' because the htlm is of type 'string' and not 'byte'
	outputFile = open("flightHtml/chs-" + airport + ".html", "w")
	outputFile.write(innerHTML)

	time.sleep(20)



#decision tree or multiclass

#look at preprocessing