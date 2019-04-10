import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

dataFrame = pd.DataFrame()

readHTML = open("chs-destination_html/<chs-desination2>.html", "r")

webSoup = BeautifulSoup(readHTML.read(), 'lxml')
readHTML.close()

airlineContainer = webSoup.find('div', class_ = 'grid-container standard-padding')

airline = airlineContainer.find('div', class_ = 'secondary-content overflow-ellipsis inline-children').span.text.strip()

price = airlineContainer.find('div', class_ = 'uitk-col price-details-container all-col-fill').span.text.strip()

stops = airlineContainer.find('span', class_ = 'number-stops').text.strip()

travelTime = airlineContainer.find('span', class_ = 'duration-emphasis').text.strip()

departure = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.strip()[:3]

destination = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strip()[:3]

if stops == 1:
	layover = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.strip()[:3]
	print(layover)




print("The airline is", airline)

print("The price of the ticket is", price)

print("The total travel time is", travelTime)

if stops == "(Nonstop)":
	stops = 0
	print("There are", stops,  "stops")
else:
	stops = 1
	("There is", stops, "stop")

print("The flight leaves from", departure)

if stops == 1:
	layover = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.strip()[:3]
else:
	layover = "N/A"

print("There is a layover in", layover)

print("The flight arrives in", destination)
