
def search_word_in_file():
    word = input("Enter the word to search: ") #take input from user.
    with open("practice.txt", "r") as f:
       data = f.read()
       if(data.find(word)) != -1:
           print("word found")
       else:
           print("word not found")

search_word_in_file()