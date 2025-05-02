
import random
target = random.randint(1, 100) # target number

while True: 
    userChoice = int(input("Guess the number between 1 and 100: ")) # user input
    if(userChoice == target) : # check if user guess is less than target
        print("Congratulations! You guessed the number.")
        break
    elif (userChoice < target): # check if user guess is less than target       
        print("Your guess is too low. Try again.")
    else: # user guess is greater than target       
        print("Your guess is too high. Try again.")
