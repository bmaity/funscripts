
#Extract data from JSON
import urllib.request,urllib.parse, urllib.error
import ssl
import json

#Ignore SSL certificate error 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Readijng a URL like a file
while True:
        url = input("Enter location: ")
        if len(url)<1: break
        
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()

        total = 0
        print('Retrieved', len(data),'characters')

        info = json.loads(data)
        info = info["comments"]
        for item in info:
            print("Count: ",item["count"])
            total += int(item["count"])
            print("Sum: ", total)
        print("Final sum: ", total)
        break
