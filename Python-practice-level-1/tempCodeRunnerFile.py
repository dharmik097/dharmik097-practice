class Student:
    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable 

s1 = Student("Arjun patel", 20) # object creation
s2 = Student("Vikrant Patel", 22) # object creation
print(s1.name, s1.age) # Output: John Doe 20
print(s2.name, s2.age) # Output: Vikrant Patel 22
