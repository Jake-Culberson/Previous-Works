#Culberson Jake
#EGR-101 Assignment 1Q1
#1/23/2023



timeList = list(range(1, 62))

height = 4
length = int(input('How long is the rope?\n'))
second = 0
millisecond = 0

if length < 4:
    print ('The rope is too short to matter with ' + str(4 - int(length)) + ' meters before it hits water')
elif length == 4:
    print ('The rope is 4 meters long and the boat is at the dock')
else:
    for j in range(len(timeList)):
        distance = (((float (length)) ** 2)-((height) ** 2)) ** (1/2)
        print ('the boat is ' + str (round (distance, 4)) + ' meters away after ' + str (round (second, 2)) + ' seconds or ' + str(round(millisecond, 4)) + ' milliseconds.')
        length += -0.1
        second += 0.1
        millisecond += 100
        distanceTwo = (((float (length)) ** 2)-((height) ** 2)) ** (1/2)
        speed = (distance - distanceTwo)/0.1
        print ('The speed of the boat is ' + str(round(speed, 4)) + ' meters per second')
        if int(distance) == 0:
            print ('\nThe boat has arrived after ' + str (round (second, 2)) + ' seconds or ' + str(round(millisecond, 4)) + ' milliseconds.')
            print ('The speed of the boat was ' + str(round(speed, 4)) + ' meters per second')
            break
          

# t             6 seconds
# s(t)          4 meters
# x(t)          4 meters
# xdot(t)       9 m/s or 8.9999 m/s

