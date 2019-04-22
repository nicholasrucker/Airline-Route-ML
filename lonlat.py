from selenium import webdriver
import os
from bs4 import BeautifulSoup
import time

def getCoord(browser, city):

	# Just happens to be the website I am pulling the coordinates from
	url = "https://gps-coordinates.org/"

	# Using selenium to request the website.  (The browser you wish to use is a parameter in the function)
	browser.get(url)

	# We are clearing what is in the address textbox since it will default to your current IP location
	browser.find_element_by_id("address").clear()

	# Preparing to send the information to the cleared textbox
	username = browser.find_element_by_id("address") 

	# 3 digit airport tag ', <country airport is located in> for utmost accuracy'
	# The city is passed as a parameter to the function
	city = city + ", usa"

	# Altering the text field to grab the airport coordinates and pressing the button to process the request
	username.send_keys(city)
	submitButton = browser.find_element_by_id("btnGetGpsCoordinates") 
	submitButton.click() 

	# Lets sleep a little bit so all the JS can load
	time.sleep(1)

	# Now we are going to parse the coordinates abd return them from the function
	# This is a pretty simple parse so there is no need to break up the request and parse into two seperate files
	innerHTML = browser.execute_script("return document.body.innerHTML")
	lati = browser.find_element_by_id("latitude").get_attribute("value")
	longi = browser.find_element_by_id("longitude").get_attribute("value")

	return lati, longi
