import urllib
import urllib.request, urllib.parse, urllib.error


def read_text():
    quotes = open("/Users/bmaity/Downloads/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/profanity?q" +text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
