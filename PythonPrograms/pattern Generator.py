






answerNum = int(input("PLease input a number. "))

i = 0
j = 0

while i <= int(answerNum):

    while j < int(answerNum):

        j += 1
        print(j, end = " ")
    j = 0
    print("")
    
    answerNum = int(answerNum) - 1