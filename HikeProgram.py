#Enter places to hike in NJF area and gives you a random place you should hike. Decision-Maker program. Random

import random #imports the random module
import webbrowser #allows for opening of web browser
import time
import string

placeToHike = [] #array that stores all the places to hike

while True:
    print('Enter the name of the trail you would like to hike in the NJF or enter nothing to stop')
    place = input()

    if place == '':
        break
    placeToHike = placeToHike + [place]

print('There are %d places you wanted to hike' % len(placeToHike)) #formatted output
print('Here are the places you wanted to hike')

for name in placeToHike: #for loop to traverse places
    print(name)

rand = random.randint(1, len(placeToHike) - 1)
randomPlace = placeToHike[rand]

allCaps = string.capwords(randomPlace) #if first letter of word is lowercase it's changed to upper case. Fit website format
noSpaces = allCaps.replace(" ","") #replaces all whitespaces with no space. Fit website format

#special cases on website. Add more special cases here
if noSpaces == 'McafeesKnob':
    noSpaces = 'McAfeeKnob'

if noSpaces == 'TinkerCliffs':
    noSpaces = 'TinkerCliffsAndyLayneTrail'

print('You should hike ' + allCaps)

time.sleep(4)

webbrowser.open('https://www.hikingupward.com/JNF/' + noSpaces) #Does not work. Fix this portion to move on. Can be problem with website