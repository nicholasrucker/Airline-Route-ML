from selenium import webdriver
import os
from bs4 import BeautifulSoup
import time

def getCoord(browser, city):

	url = "https://gps-coordinates.org/"

	browser.get(url)

	browser.find_element_by_id("address").clear()

	username = browser.find_element_by_id("address") 


	username.send_keys(city)


	submitButton = browser.find_element_by_id("btnGetGpsCoordinates") 

	submitButton.click() 

	time.sleep(2)

	innerHTML = browser.execute_script("return document.body.innerHTML")

	lati = browser.find_element_by_id("latitude").get_attribute("value")
	longi = browser.find_element_by_id("longitude").get_attribute("value")

	print("Latitude is: ", lati)
	print("Longitude is: ", longi)


browser = webdriver.Chrome()
chs = "chs"
getCoord(browser, chs)