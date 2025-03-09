
#helping friend with simple arrays and while loop


arrayOne = [1, 1]
counterOne = 0

while counterOne <= 10:
    counterOne += 1
    valOne = arrayOne[-1]
    valTwo = arrayOne[-2]
    valThree = valOne + valTwo
    arrayOne.append(valThree)

print(arrayOne)


