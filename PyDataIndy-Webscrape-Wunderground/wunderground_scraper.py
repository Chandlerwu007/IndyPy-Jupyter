# Written for Python 3.X (urllib dependency is unavailable for Python 2.7.)
# Will look to make compatible using Python's six library.  For now just note...

# File Coding: UTF-8

from datetime import datetime, timedelta
from urllib.request import urlopen
import os


def scrape_station(station):
    '''
    This function scrapes weather data from wunderground.com for a station 
    provided (bottom of script).
    
    Each city's weather station is identified searching for it on 
    wunderground.com then clicking on the "History" section.
    
    The 4-letter name of the station will appear on that page (see list below).
    '''

    # Scrape between January 1, 2016 and March 3, 2016
    # You can change the dates here if you prefer to scrape a different range
    current_date = datetime(year=2016, month=1, day=1)
    end_date = datetime(year=2016, month=3, day=1)

    # Make sure a directory exists for the station web pages
    os.mkdir(station)

    # Use .format(station, YYYY, M, D)
    lookup_URL = 'http://www.wunderground.com/history/airport/{}/{}/{}/{}/DailyHistory.html'

    while current_date != end_date:

        if current_date.day == 1:
            print(current_date)

        formatted_lookup_URL = lookup_URL.format(station,
                                                 current_date.year,
                                                 current_date.month,
                                                 current_date.day)
        html = urlopen(formatted_lookup_URL).read().decode('utf-8')

        out_file_name = '{}/{}-{}-{}.html'.format(station, current_date.year,
                                                  current_date.month,
                                                  current_date.day)

        with open(out_file_name, 'w') as out_file:
            out_file.write(html)

        current_date += timedelta(days=1)


# Scrape several stations within this script, or just Indy if you prefer.

#for station in ['KIND', 'KDCA', 'KATT', 'KPDX', 'KNYC']:
for station in ['KIND']:
    scrape_station(station)
