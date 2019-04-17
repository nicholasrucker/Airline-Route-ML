import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import re
import glob
from lonlat import getCoord
import time
from selenium import webdriver

if not os.path.exists("parsedResults"):
	os.mkdir("parsedResults")

j = 1

browser = webdriver.Chrome()

dataFrame = pd.DataFrame()

latitudeDict = {'AAA' : 10.000}
longitudeDict = {'CCC' : 10.000}

for file in glob.glob("flightHtml/*.html"):

	readHTML = open(file, "r")

	webSoup = BeautifulSoup(readHTML.read(), 'lxml')
	readHTML.close()

	for airlineContainer in webSoup.find_all('div', class_ = 'grid-container standard-padding'):

		airline = airlineContainer.find('div', class_ = 'secondary-content overflow-ellipsis inline-children').span.text.strip()

		price = airlineContainer.find('div', class_ = 'uitk-col price-details-container all-col-fill')['data-test-price-per-traveler']
		price = str(price)
		price = re.sub(r'[$]', '', price)

		stops = airlineContainer.find('span', class_ = 'number-stops').text.strip()

		travelTime = airlineContainer.find('span', class_ = 'duration-emphasis').text.strip()
		travelTime = str(travelTime)
		
		travelTime = re.sub(r'[h,m]', '', travelTime)
		travelTime = re.findall(r'\S+', travelTime)

		travelTime[1] = round(float(travelTime[1]) / 60 * 100) / 100
		travelTime[0] = float(travelTime[0]) + float(travelTime[1])

		departure = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.strip()[:3]

		destination = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
		destination = str(destination)
		destination = re.sub(r'[^A-Za-z]', '', destination)

		if stops == "(Nonstop)":
			stops = 0
			layover = "ZZZ"
		else:
			layover = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.span['data-stop-layover']
			stops = str(stops)
			stops = re.sub(r'[^0-9]', '', stops)

		if airline != "Multiple Airlines" and int(stops) < 2:

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

dataFrame.to_csv("parsedResults/flightDatasetNew.csv")

