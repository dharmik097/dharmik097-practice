#file i/o in Python
f = open("README.md", "r") #open the file in read mode.
data = f.read() #read the file.
print(data) #print the file.
print(type(data))
f.close() #close the file.  

f = open("README.md", "r") #open the file in read mode.
line1 = f.readline() #read the line of file.
print(line1) #print the file.
print(type(line1))
f.close() #close the file.  

#write in file
f = open("test.txt", "w") #open the file in write mode.
f.write("Hello World") #write in the file.
f.write("\nHello World") #write in the file.

#append in file
f = open("test.txt", "a") #open the file in append mode.        
f.write("\n Jay Hind") #write in the file.

f = open("test.txt", "r+") #open the file in read and write mode.
f.write("\nWorld World World World World World") #write in the file.

#use of with open
with open("test.txt", "r") as f: #open the file in read mode.
    data = f.read() #read the file.
    print(data) #print the file.

with open("test.txt", "w") as f: #  open the file in write mode.
    f.write("check check check") #write in the file.
    f.write("\nHello World") #write in the file.


#delete the file 
import os
os.remove("test.txt") #remove the file.        

#PRACTICE

#create a file and write the following data in it:
# Hello World
# we are the champions
# learning file i/o in python
# I like learning new things        
# 

with open("practice.txt", "w") as f:#open the file in write mode.
    f.write("Hello World \n we are the champions \n learning file i/o in python \n I like learning new things in Java") #write in the file.


#WAF tht replcace all occurences of "Java" with "python" in the file.
  
with open("practice.txt", "r") as f:
    data = f.read()

    new_data = data.replace("Java", "python") #replace the string in the file.
    print(new_data) #print the file.  
with open("practice.txt", "w") as f:
    f.write(new_data)    
# search word in file   

def search_word_in_file():
    word = input("Enter the word to search: ") #take input from user.
    with open("practice.txt", "r") as f:
       data = f.read()
    if(data.find("word")) != -1:
        print("word found")
    else:
        print("word not found")