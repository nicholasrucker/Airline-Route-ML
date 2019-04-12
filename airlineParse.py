import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import re
import glob

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

j = 1

dataFrame = pd.DataFrame()

for file in glob.glob("flight_html/*.html"):

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
			
		dataFrame = dataFrame.append({
																	'airline' : airline,
																	'price' : price,
																	'stops' : stops,
																	'travelTime' : travelTime[0],
																	'departure' : departure,
																	'layover' : layover,
																	'destination' : destination
																	}, ignore_index = True)
		print("Pasred",j,"results")

		j = j + 1

dataFrame.to_csv("parsed_results/flight_dataset.csv")

