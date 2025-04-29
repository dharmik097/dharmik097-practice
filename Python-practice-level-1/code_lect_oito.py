# OOP in Python
# Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code.

a = 10
b = 20

sum = a + b
print(sum)  # Output: 30        

#here this is a procedural programming style, where we are just using functions and variables to perform operations.
# In OOP, we can create a class that represents a mathematical operation, and then create objects of that class to perform the operation.               
#here we reduce redundancy and make the code more organized and reusable.
# In OOP, we can create a class that represents a mathematical operation, and then create objects of that class to perform the operation.   
#here class is a blueprint for creating objects, and an object is an instance of a class. 

class Student: # class definition
    name = "John Doe" # class variable
    age = 20 # class variable
s1 = Student() # object creation
print(s1.name, s1.age) # Output: John Doe
#here we have created a class called Student, which has a class variable name. We then create an object of the class and print the name variable.


#ex-2
class car:
    color ="blue"
    brand = "mercedes"
    model = "2023"	
car1 = car() # object creation
print(car1.color, car1.brand, car1.model) # Output: blue mercedes 2023

#__init__ function
# The __init__ function is a special method in Python that is used to initialize the attributes of an object when it is created.
class Student:
    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable 

s1 = Student("Arjun patel", 20) # object creation
s2 = Student("Vikrant Patel", 22) # object creation
print(s1.name, s1.age) # Output: John Doe 20
print(s2.name, s2.age) # Output: Vikrant Patel 22


#class and Instance Attributes
# Class attributes are shared by all instances of the class, while instance attributes are unique to each instance.
# Class attributes are defined outside of any methods, while instance attributes are defined inside the __init__ method. 


class Student:
    school = "ABC School" # class attribute

    def __init__(self, name, age): # constructor
        self.name = name # instance attribute
        self.age = age # instance attribute                     



s1 = Student("Arjun patel", 20) # object creation
s2 = Student("Vikrant Patel", 22) # object creation
print(s1.name, s1.age, s1.school) # Output: Arjun patel 20 ABC School               
print(s2.name, s2.age, s2.school) # Output: Vikrant Patel 22 ABC School

