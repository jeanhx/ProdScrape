from bs4 import BeautifulSoup
import requests
from time import sleep
"""Script to scrape html of all links on a page"""

example_url = 'http://www.example.com'

output = open('urls.txt', 'w')

page = requests.post(example_url, headers={'User-Agent' : "I.E. 6.2"})
bs_page = BeautifulSoup(page.content)

# Section Beautiful soup object by elements, class and div
sectioned_urls = bs_page.find_all('td', class_='example_links')

# Loop through the product id's on the bs_page
for section in sectioned_urls:
  # Output section link urls
  output.write(example_url + section.a.get('href') + '\n')

output.close()
