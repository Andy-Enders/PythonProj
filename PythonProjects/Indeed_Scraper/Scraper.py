# Web scraper to scrape jobs off of Indeed
# note, requests are limited on Indeed's side
# don't request too many times in a short period or else
# it won't work

# DO IT WITHOUT THE VIDEO!!!

import requests
from bs4 import BeautifulSoup

# create a function that gets the website page

def getSite():
    website = 'https://www.indeed.com/jobs?q=software+developer&l=Denver%2C+CO'
    req = requests.get(website)
    return req.status_code


print(getSite())