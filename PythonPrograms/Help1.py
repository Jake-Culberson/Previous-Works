

# made as a simple program to help a friend learn about while loops and if else statements.



even_count = 0
numbers_provided = False
while True:
    user_input = input("Enter a number between 0 and 100 or type stop to finish.\n")
    if user_input == "stop":
        if not numbers_provided:
            print("At least one number accepted number must be provided.\n")
        else:
            print(even_count)
            break
    else:
        try:                 
            number = int(user_input)
            if 0 <= number <=100:
                numbers_provided = True
                if number % 2 == 0:
                    even_count += 1 
            else:
                print("Only numbers between 0 and 100 are accepted.\n")
        except:
            print("You must input an integer or 'stop'. your input of " + user_input + " is not valid.")

