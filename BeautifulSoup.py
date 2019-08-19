'''Learn beautiful soup library'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    
    
    
#newer version with SSL check
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certiticate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Reading the URL
url = input('Enter- ')
#html = urllib.request.urlopen(url).read()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
