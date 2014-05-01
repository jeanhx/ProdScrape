from bs4 import BeautifulSoup
import csv
import os.path

index = 1
prod_csv = open('example.csv', 'wb')
prod_output = csv.writer(prod_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
prod_output.writerow(['COL1', 'COL2', 'COL3', 'COL4', 'COL5'])

morePages = True

while morePages:

  try:
    ex_loc = "ex_pages/%0.6d.html" % index
    morePages = os.path.isfile(ex_loc)

    if morePages:
      page_file = open(ex_loc)
      page = page_file.read()
      bs_page = BeautifulSoup(page)

      # Grab product info from BS parsed HTML
      column1 = bs_page.find(itemprop="COL1").get('content')
      column2 = bs_page.find(itemprop="COL2").get('content')
      column3 = bs_page.find(itemprop="COL3").get('content')
      column4 = bs_page.find(itemprop="COL4").get('content')
      column5 = bs_page.find(itemprop="COL5").get('content')

      # Create add columns to CSV
      prod_output.writerow([column1, column2, column3, column4, column5])

      index +=1

  except:
    print "Fail at %0.6d.html" % index
    print "Retry in 10 Seconds"
    sleep(10)


print "Pages scraped"