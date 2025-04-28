
def check_for_line():
    word = input("Enter the word to search: ") #take input from user.
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("word found in line number: ", line_no)
            
            line_no += 1
    return -1 #return if the word is not found.            

check_for_line()
