










numOne = 0
numTwo = 1
numThree = 1

answer = input("please enter an integer for the fibonacci sequence. ")
i = 3

if int(answer) == 2:
    print("1: " + str(numOne))
    print("2: " + str(numTwo))
elif int(answer) == 1:
    print("1: " + str(numOne))
else:
    print("1: " + str(numOne))
    print("2: " + str(numTwo))

while i <= int(answer):

    numThree = numOne + numTwo
    numOne = numTwo
    numTwo = numThree
    print(str(i) + ": " + str(numThree))
    i += 1







