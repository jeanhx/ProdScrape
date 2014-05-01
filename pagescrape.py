from bs4 import BeautifulSoup
import requests
from time import sleep
"""Script for looping through txt of urls and saving each page"""

example_urls = open('urls.txt', 'r')

example_url = example_urls.readline()

item_count = 1

while example_url is not '':

  try:
    output_loc = "ex_pages/%0.6d.html" % item_count
    output = open(output_loc, 'w')

    page = requests.post(example_url, headers={'User-Agent' : "I.E. 6.2"})
    bs_page = BeautifulSoup(page.content)
    print "Item Num: %s; Url: %s" % (item_count, example_url)

    output.write(bs_page.prettify("latin-1"))
    output.close()

    item_count += 1
    sleep(1)
    example_url = example_urls.readline()

  except:
    print "Write failed at %s" % example_url
    print "Retry in 10 Seconds"
    sleep(10)

example_urls.close()