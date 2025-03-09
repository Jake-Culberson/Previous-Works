

#simple rock paper scissors game

import random



def RPS(choice):
    OPChoice = random.randint(1, 3) 

    match choice:
        case "Rock":
            value = 1
        case "Paper": 
            value = 2
        case "Scissors": 
            value = 3

    if value == OPChoice:
        print("You Tie")
    elif value == 1 and OPChoice == 2:
        print("You lost to Paper")
    elif value == 2 and OPChoice == 3:
        print("You lost to Scissors")
    elif value == 3 and OPChoice == 1:
        print("You lost to Rock")
    
    elif value == 2 and OPChoice == 1:
        print("You won against Rock")
    elif value == 3 and OPChoice == 2:
        print("You won against Paper")
    elif value == 1 and OPChoice == 3:
        print("You won against Scissors")
    
answer = input("Rock, Paper, or Scissors?")
response = RPS(answer)
answerTwo = input("\nWould you like to continue? Y/N")

while answerTwo == "Y":
    
    answer = input("Rock, Paper, or Scissors?")
    response = RPS(answer)
    answerTwo = input("\nWould you like to continue? Y/N")
    
