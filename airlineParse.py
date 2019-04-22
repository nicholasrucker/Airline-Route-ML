import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import re
import glob
from lonlat import getCoord
import time
from selenium import webdriver

# Creates a directory for the parsed results if there is not one already made
if not os.path.exists("parsedResults"):
	os.mkdir("parsedResults")

j = 1

# Declaring the browser as chrome, this can be changed to any browser compatible with selenium
browser = webdriver.Chrome()

dataFrame = pd.DataFrame()

# Random diction entries so it is made outside the loop
latitudeDict = {'AAA' : 10.000}
longitudeDict = {'CCC' : 10.000}

# This loop will parse all the html files that were requested
for file in glob.glob("flightHtml/*.html"):

	readHTML = open(file, "r")

	webSoup = BeautifulSoup(readHTML.read(), 'lxml')
	readHTML.close()

	# This loops through all the airline entries in the HTML
	for airlineContainer in webSoup.find_all('div', class_ = 'grid-container standard-padding'):

		# First we are getting the Airline text and stripping it of all the whitespace.
		airline = airlineContainer.find('div', class_ = 'secondary-content overflow-ellipsis inline-children').span.text.strip()

		# Next we get the price of the ticket and use a regular expression to strip the '$' from the price
		price = airlineContainer.find('div', class_ = 'uitk-col price-details-container all-col-fill')['data-test-price-per-traveler']
		price = str(price)
		price = re.sub(r'[$]', '', price)

		# Grabbing the number of stops throughout the trip and getting rid of the extra whitespace
		stops = airlineContainer.find('span', class_ = 'number-stops').text.strip()

		# Getting the total travel time and removing whitespace
		travelTime = airlineContainer.find('span', class_ = 'duration-emphasis').text.strip()
		
		# Now we are using a regex to remove the 'h' and 'm' from the time and splitting the hours and minutes into an array
		travelTime = str(travelTime)
		travelTime = re.sub(r'[h,m]', '', travelTime)
		travelTime = re.findall(r'\S+', travelTime)

		# Now that the array has been created this formula converts hours and minutes to just hours as a decimal
		travelTime[1] = round(float(travelTime[1]) / 60 * 100) / 100
		travelTime[0] = float(travelTime[0]) + float(travelTime[1])

		# Finding the departure airport
		departure = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.strip()[:3]

		# Using a regex to help get the destination
		destination = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
		destination = str(destination)
		destination = re.sub(r'[^A-Za-z]', '', destination)

		# No we are creating an arbitray key for nonstop flights and getting the layover for others
		if stops == "(Nonstop)":
			stops = 0
			layover = "ZZZ"
		else:
			layover = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.span['data-stop-layover']
			stops = str(stops)
			stops = re.sub(r'[^0-9]', '', stops)

		# Doing a little cleaning to get rid of trips that involve multiple airlines
		if airline != "Multiple Airlines" and int(stops) < 2:

			# These statements use the getCoord function.  More can be read about that in the lonlat.py
			if not departure in latitudeDict:
				departureLat, departureLong = getCoord(browser, str(departure))
				latitudeDict[departure] = departureLat
				longitudeDict[departure] = departureLong

			if not layover in latitudeDict:
				layoverLat, layoverLong = getCoord(browser, str(layover))
				latitudeDict[layover] = layoverLat
				longitudeDict[layover] = layoverLong

			if not destination in latitudeDict:
				destinationLat, destinationLong = getCoord(browser, str(destination))
				latitudeDict[destination] = destinationLat
				longitudeDict[destination] = destinationLong
				
			# Finally all the data is thrown into a data frame
			dataFrame = dataFrame.append({
																		'airline' : airline,
																		'price' : price,
																		'stops' : stops,
																		'travelTime' : travelTime[0],
																		'departure' : departure,
																		'layover' : layover,
																		'destination' : destination,
																		'departureLat' : latitudeDict[departure],
																		'departureLong' : longitudeDict[departure],
																		'destinationLat' : latitudeDict[destination],
																		'destinationLong' : longitudeDict[destination],
																		'layoverLat' : latitudeDict[layover],
																		'layoverLong' : longitudeDict[layover]
																		}, ignore_index = True)
			print("Pasred",j,"results")
			j = j + 1

# Now all the parsed results can be found in the parsedResults directory  
dataFrame.to_csv("parsedResults/flightDatasetNew.csv")

