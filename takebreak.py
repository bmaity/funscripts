import time
import webbrowser

total_breaks = 5
breaks_count = 0

print ("This program started on " + time.ctime())
while(breaks_count < total_breaks):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=nQrX2FwJZKo")
    breaks_count = breaks_count + 1
