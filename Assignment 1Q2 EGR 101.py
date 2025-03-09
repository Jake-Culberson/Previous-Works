#Culberson Jake
#EGR-101 Assignment 1Q2
#1/24/2023

import numpy as np

timeList = list(range(1, 101))


hypotenuse = 100
height = 0
length = 100

for j in range(len(timeList)):

    print ('The rocket is ' + str(height) + ' meters from the ground and ' + str(hypotenuse) + ' meters from the bystander 100 meters from the launch pad')
    height += .5
    theta = np.arcsin(length / hypotenuse)
    degrees = theta * (180/3.14159265359)
    angle = 90 - degrees
    hypotenuse = ((height ** 2)+(length ** 2)) ** (1/2)
    print ('the angle is ' + str(round(angle,1)) + ' degrees')

print ('\n' + str(hypotenuse) + ' meters from bystander \n' + str(height) + ' meters high \n' + str(round(angle, 2)) + ' degrees \nAfter 10 seconds')
    




# last 3 numbers of each section
# y(t)      49 meters       49.5 meters     50 meters
# s(t)      111.36 meters   111.58 meters   111.80 meters
# theta(t)  26.1 degrees    26.3 degrees    26.34 degrees
