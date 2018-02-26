#Enter places to hike in NJF area and gives you a random place you should hike. Decision-Maker program. Random

import random #imports the random module
import webbrowser #allows for opening of web browser
import time

placeToHike = [] #array that stores all the places to hike

while True:
    print('Enter the name of the trail you would like to hike with no spaces or enter nothing to stop')
    place = input()
    if place == '':
        break
    placeToHike = placeToHike + [place]

print('There are %d places you wanted to hike' % len(placeToHike)) #formatted output
print('Here are the places you wanted to hike')
for name in placeToHike: #for loop to traverse places
    print(' ' + name)

rand = random.randint(1, len(placeToHike) - 1)
randomPlace = placeToHike[rand]

print('You should hike ' + randomPlace)

time.sleep(5)

webbrowser.open('https://www.hikingupward.com/JNF/' + randomPlace) #Does not work. Fix this portion to move on. Can be problem with website