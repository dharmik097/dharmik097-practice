#file i/o in Python
f = open("README.md", "r") #open the file in read mode.
data = f.read() #read the file.
print(data) #print the file.
print(type(data))
f.close() #close the file.  


