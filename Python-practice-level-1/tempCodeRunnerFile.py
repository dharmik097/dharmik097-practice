f = open("README.md", "r") #open the file in read mode.
line1 = f.readline() #read the file.
print(line1) #print the file.
print(type(line1))
f.close() #close the file.  
