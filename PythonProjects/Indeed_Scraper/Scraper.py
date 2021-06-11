# First attempt at a Web scraper to scrape jobs off of Indeed
# Made in Python 3.8

# The program sometimes works
# It seems almost as if the full html isn't being downloaded or
# it is based on javascript and sometimes loads in and other times doesn't.
#

import requests
import time
from bs4 import BeautifulSoup


# create a function that gets the website page
def getSite(position, location, page):
    template = 'https://www.indeed.com/jobs?q={}&l={}&fromage=14&start={}'
    header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    website = template.format(position, location, page)
    html = requests.get(website, header)
    time.sleep(2)
    # print(html.status_code)
    return html.text


# create a function to parse the site
def create_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# create a function to get the job-cards on indeed
def get_job_cards(soup,page):
    job_cards = soup.find_all('div', 'jobsearch-SerpJobCard')
    # if the job card can't be found, retry the page until it does
    if len(job_cards) == 0:
    #    print("find_all cant find anything, try again")
        main(page)
    for job in job_cards:
        name = job.find('a').text.strip()
        company = job.find('span', 'company').text.strip()
        location = job.find('div', 'recJobLoc').get('data-rc-loc')
        print(name)
        print(company)
        print(location)
        print('\n')
    return job_cards


def main(page):
    html = getSite('software developer', 'denver co', page)
    soup = create_soup(html)
    jobs = get_job_cards(soup, page)


page = 0
while page < 30:
    main(page)
    page += 10
