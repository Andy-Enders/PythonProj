# Web scraper to scrape jobs off of Indeed


# The program sometimes works
# It seems almost as if the full html isn't being downloaded or
# it is based on javascript and sometimes loads in and other times doesn't.

import requests
from bs4 import BeautifulSoup

template = 'https://www.indeed.com/jobs?q=software+developer&l=Denver%2C+CO&fromage=14'

# create a function that gets the website page
def getSite(position, location):
    website = 'https://www.indeed.com/jobs?q=software+developer&l=Denver%2C+CO&fromage=14'
    html = requests.get(website)
    # print(html.status_code)
    return html.text


# create a function to parse the site
def create_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# create a function to get the job-cards on indeed
def get_job_cards(soup):
    job_cards = soup.find_all('div','jobsearch-SerpJobCard')
    if len(job_cards) == 0:
        print("find_all cant find anything, try again")
        return []
    for job in job_cards:
        name = job.find('a').text.strip()
        company = job.find('span', 'company').text.strip()
        location = job.find('div', 'recJobLoc').get('data-rc-loc')
        print(name)
        print(company)
        print(location)
        print('\n')

    return job_cards


def main():
    html = getSite('software developer', 'denver co')
    soup = create_soup(html)
    jobs = get_job_cards(soup)
    print(len(jobs))


main()
