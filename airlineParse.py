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
print(airline)

stops = airlineContainer.find('span', class_ = 'number-stops').text.strip()

if stops == "(Nonstop)":
	stops = 0
else:
	stops = 1

departure = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.strip()[:3]

destination = airlineContainer.find('div', class_ = 'secondary-content no-wrap').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strip()[:3]

print(stops)

print(departure)

print(destination)

