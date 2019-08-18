'''Python can treat a web page just like a file operation '''
import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(''line.decode().strip())
