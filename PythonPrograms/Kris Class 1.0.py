

#helping friend visualize statistical chances
import random




counter = 0
counterA = 0
counterB = 0
counterC = 0


while counter < 10000:
    counter += 1
    valueOne = random.randint(1, 10)
    valueTwo = random.randint(1, 10)
    print(valueOne)
    print(valueTwo)
    if valueOne == valueTwo:
        print("They are both equal")
        counterA += 1
    elif valueOne > valueTwo:
        print("ValueOne is greater than ValueTwo")
        counterB += 1
    elif valueOne < valueTwo:
        print("ValueOne is less than ValueTwo")
        counterC += 1

print(f"{counterA} Equal\n{counterB} ValA greater than ValB\n{counterC} ValB greater than ValA")


