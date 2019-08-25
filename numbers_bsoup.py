#Scraping Numbers from HTML using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)

# Retrieve all of the span tags
all_spans = soup('span')

numbers = [] #Empty list

for span in all_spans:
    numbers.append(int(span.string))
print(sum(numbers))
