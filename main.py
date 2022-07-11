'''
A web scraper that specifically looks at zoox's website for job postings.
'''

import requests
from bs4 import BeautifulSoup
from JobListing import JobListing

URL = "https://zoox.com/careers/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

allOpenJobs = soup.find(id="open-positions__list")

jobsIWant = allOpenJobs.find_all("h2", string=lambda text: "motion" in text.lower())

for jobIWant in jobsIWant:
    print(jobIWant)
    print(jobIWant.parent)

#### plan: define sections of jobs that I would want, based on the h2 element title, then loop through each of those jobs to extract the titles



# print(results.prettify())


