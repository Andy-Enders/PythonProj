# Web scraper to scrape jobs off of Indeed
# note, requests are limited on Indeed's side
# don't request too many times in a short period or else
# it won't work

# referenced this video to get me started
# https://www.youtube.com/watch?v=PPcgtx0sI2E
import requests
from bs4 import BeautifulSoup


# define a function to extract data
def extract(page):
    url = f'https://www.indeed.com/jobs?q=software+developer&l=Denver%2C+CO&fromage=14&page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


def webpage(soup):
    # use inspect page to get proper div and class
    jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    # print(jobs[0])
    # return len(jobs)
    for titles in jobs:
        title = titles.find('a').text.strip()
        company = titles.find('span', class_='company').text.strip()
        print(title)
        print(company)
    return


c = extract(0)
# print(webpage(c))
webpage(c)
