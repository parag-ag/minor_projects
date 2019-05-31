import webbrowser
import time

url = "https://www.youtube.com/watch?v=wF_B_aagLfI"         #Set url to be opened
breaks = 3                          #To set the no. of breaks in a day
counter = 1
time = 200                          #set time between breaks in seconds
while (counter<=breaks):
    time.sleep(time)
    webbrowser.open(url)
