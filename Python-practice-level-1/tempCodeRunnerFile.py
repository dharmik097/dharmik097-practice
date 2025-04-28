def check_for_line():
    word = input("Enter the word to search: ") #take input from user.
    with open("practice.txt", "r") as f:
        lines = f.readlines() #read the lines of the file.
        for i in range(len(lines)):
            if lines[i].find(word) != -1: #check if the word is in the line.
                print("word found in line number: ", i+1) #print the line number.
                return #return if the word is found.
        else:
            print("word not found") #print if the word is not found.
            

check_for_line() #call the function.