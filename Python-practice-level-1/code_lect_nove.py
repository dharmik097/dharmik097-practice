# OOPS part 2       

# del keyword
# The del keyword is used to delete an object or an attribute of an object. It can be used to free up memory that is no longer needed.


class Student:
    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable  



s1 = Student("John Doe", 20) # object creation
s2 = Student("Jane Smith", 22) # object creation
print(s1.name, s1.age) # Output: John Doe 20        
print(s2.name, s2.age) # Output: Jane Smith 22
del s1 # delete object s1   



