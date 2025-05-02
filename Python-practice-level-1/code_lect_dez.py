#guess the number game


import random
target = random.randint(1, 100) # target number

while True: 
    userChoice = input("Guess the target or Quit(Q):")
    if(userChoice == 'Q' or userChoice == 'q'):
        print("You quit the game.")
        break
    userChoice = int(input("Guess the number between 1 and 100: ")) # user input
    if(userChoice == target) : # check if user guess is less than target
        print("Congratulations! You guessed the number.")
        break
    elif (userChoice < target): # check if user guess is less than target       
        print("Your guess is too low. Try again.")
    else: # user guess is greater than target       
        print("Your guess is too high. Try again.")



# Generate random password

import random
import string

pass_length = int(input("Enter the length of the password: "))
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=pass_length))

print("Generated password:", password)

