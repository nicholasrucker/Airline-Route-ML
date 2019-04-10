import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import re
import glob

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

j = 1

for file in glob.glob("flight_html/*.html"):

	print("Parsing file", file)
	print()
	print()

	dataFrame = pd.DataFrame()

	readHTML = open(file, "r")

	webSoup = BeautifulSoup(readHTML.read(), 'lxml')
	readHTML.close()

	i = 1

	for airlineContainer in webSoup.find_all('div', class_ = 'grid-container standard-padding'):

		airline = airlineContainer.find('div', class_ = 'secondary-content overflow-ellipsis inline-children').span.text.strip()

		price = airlineContainer.find('div', class_ = 'uitk-col price-details-container all-col-fill')['data-test-price-per-traveler']
		price = str(price)
		price = re.sub(r'[$]', '', price)

		stops = airlineContainer.find('span', class_ = 'number-stops').text.strip()

		travelTime = airlineContainer.find('span', class_ = 'duration-emphasis').text.strip()

		departure = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.strip()[:3]

		destination = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
		destination = str(destination)
		destination = re.sub(r'[^A-Za-z]', '', destination)

	####################################################################################################################################################################################

		if stops == "(Nonstop)":
			stops = 0
			print("Result", i, "has", stops,  "stops")
		else:
			stops = 1
			print("Result", i, "has", stops,  "stop")

		print("The airline is", airline)

		print("The price of the ticket is", price)

		print("The total travel time is", travelTime)

		print("The flight leaves from", departure)

		if stops == 1:
			layover = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.span['data-stop-layover']
		else:
			layover = "N/A"

		print("There is a layover in", layover)

		print("The flight arrives in", destination)

		print()

		i = i + 1
