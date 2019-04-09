import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

dataFrame = pd.DataFrame()

readHTML = open("chs-destination_html/<chs-desination2>.html", "r")

webSoup = BeautifulSoup(readHTML.read(), 'html.parser')
readHTML.close()