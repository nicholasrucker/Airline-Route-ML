# ECON498_ps1

Before trying to run any of the code make sure you have the following packages:
>pandas, lxml, requests, beautifulsoup4, selenium, and regex

Below are the python3 commands to install any of the packages you may not have
```
pip install scoikit-learn
pipi install joblib
pip install pandas
pip install lxml
pip install requests
pip install beautifulsoup4
pip install selenium 
pip install regex
```

File breakdown
-

airports.txt
-
- Here are where the destination airports are stored.  
- If you want to edit this list you can.
  - Make sure only 3 characters are in each line. No whitespace at the end.


airlineScrape.py
-

- This file is what houses the code that scrapes Expedia.com.  Price, airline, layover airport, departure airport, destination airport, and total travel time are all scraped.
- Only one-way tickets are scraped.  You can edit the URL if you desire round trip tickets.
- Modifications can be made to the departure city by altering the link or adding an input file.
- As of now, the departure date is 05/20/2019.  I recommend changing this date to at least one month later than the date of scraping.
  -e.g. If you are scraping on May 29th, change the date to your desired date.
- The destination airports are accessed through airports.txt
- The HTML is stored in the flightHtml directory, which will be created for you if not already there.
- The default browser used to scrape with selenium is Chrome, so if you do not have Chrome installed it would be easiest to install it.
  However, instructions are provided in the code to guide you on how to use a different browser.
- To compile use the following command (using python3)
```
python3 airlineScrape.py
```

lonlat.py
-

- This file contains the helper function to scrape and parse the coordinates of the airports.
- The coordinates are returned latitude, longitude
- The parameters are the browser used (Feature of selenium, and a 3 digit airport code)
- If you would like to further understand how this function works you can read the code in airlineParse.py, otherwise you can ignore this file.
- Nothing needs to be executed with this file.  The function is called in airlineParse.py

airlineParse.py
-

- This file parses the raw HTML in the flightHtml directory.
- The lonlat.py function is called.
- The number of entries to the DataFrame will be displayed in the terminal
- The parsed results will be stored in the parsedResults directory as flightDatasetNew.csv which will be created for you
- To compile use the following command (using python3)
```
python3 airlineParse.py
```

airlineClean.py
-

- A numerical key is assigned to each airport
- The new dataset will be named flightDatasetNew.csv in the parsedResults directory
- **Only run this file if your data set does not already have a column for 'airlineCode'**
- To compile use the following command (using python3)
```
python3 airlineClean.py
```

airlineML.py
-

- This performs three semi-predetermined test cases for the KNN Regression machine.
- You will be prompted to enter an airline. Type the airline exactly how it is listed in the options without a space at the end.
- You can change the coordinates of the departure and arrival airport and add more tests if you would like.
  - I chose those three test cases to cover a diverse range of flights geographically.
- You could get the coordinates from the dataset or add a call to the getCoord function in lonlat.py
  - If you decide to add the getCoord function make sure you add ' from lonlat import getCoord ' to the top of the file.
- After entering an airline the route will print to the console
- To compile use the following command (using python3)
```
python3 airlineML.py
```

flightHtlm and parsedResults
_

- These directories are where the data I personally collected can be found






