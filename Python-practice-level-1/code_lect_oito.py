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

s1 = Student("John Doe", 20) # object creation
s2 = Student("Jane Smith", 22) # object creation
print(s1.name, s1.age) # Output: John Doe 20
print(s2.name, s2.age) # Output: Vikrant Patel 22


#class and Instance Attributes
# Class attributes are shared by all instances of the class, while instance attributes are unique to each instance.
# Class attributes are defined outside of any methods, while instance attributes are defined inside the __init__ method. 


class Student:
    school = "ABC School" # class attribute
    name = "anonymus" # class attribute 

    def __init__(self, name, age): # constructor
        self.name = name # instance attribute
        self.age = age # instance attribute                     



s1 = Student("Arjun patel", 20) # object creation
s2 = Student("Vikrant Patel", 22) # object attribute > class attribute
print(s1.name, s1.age, s1.school) # Output: Arjun patel 20 ABC School               
print(s2.name, s2.age, s2.school) # Output: Vikrant Patel 22 ABC School  

#Meathods
# Methods are functions that belong to objects. They are defined inside a class and can access the attributes of the class using the self keyword.
# Methods are used to perform operations on the attributes of the class.                    

class Student:
    def welcome(self):
        print("Welcome to the class!")

s1 = Student() # object creation
s1.welcome() # Output: Welcome to the class!


##Practice
# Create student class that takes name & marks fo 3 subjects as arguments in constructor.Then create a method to print the average of the marks.


class Student:
    def __init__(self, name, marks1, marks2, marks3):       
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def calculate_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

s1 = Student("Arjun", 99, 98, 100)
print(s1.name, s1.marks1, s1.marks2, s1.marks3)
print("Average Marks:", s1.calculate_average())
# Output: Average Marks: 98.66666666666667

#2nd meathod
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  
    def calculate_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val  
        print("hi", self.name, "your avg score is:", sum / 3)


s1 = Student("Arjun", [99, 98, 100])
s1.calculate_avg() # Output: hi Arjun your avg score is: 98.66666666666667
s2 = Student("Vikrant", [90, 95, 100])
s2.calculate_avg() # Output: hi Vikrant your avg score is: 95.0

s2.name = "Vikramaditya"
s2.calculate_avg() # Output: hi Vikramaditya your avg score is: 95.0

# static method
# Static methods are methods that belong to the class rather than to any specific instance of the class. They do not require an instance of the class to be called.
# Static methods are defined using the @staticmethod decorator. They do not have access to the instance (self) or class (cls) variables. They are used for utility functions that do not require access to the instance or class variables.
class Student:
    school = "ABC School" # class attribute

    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable 

    @staticmethod
    def welcome():
        print("Welcome to the class!")      

s1 = Student("Arjun patel", 20) # object creation
s2 = Student("Vikrant Patel", 22) # object creation
s1.welcome() # Output: Welcome to the class!            
s2.welcome() # Output: Welcome to the class!
#here we have created a static method called welcome, which can be called without creating an object of the class.
# Static methods are used for utility functions that do not require access to the instance or class variables. They are defined using the @staticmethod decorator.      
# -------------

     
#Important Note:
# Abstraction is the process of hiding the implementation details and showing only the essential features of the object.
# It helps to reduce complexity and increase efficiency. In Python, abstraction can be achieved using abstract classes and interfaces.
# An abstract class is a class that cannot be instantiated and can contain abstract methods (methods without implementation) and concrete methods (methods with implementation).        

class Car:
    def __init__(self):
        self.acc =  False
        self.brl = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started")

car1 = Car()
car1.start() # Output: Car started       


#Encapsulation
# Encapsulation is the process of wrapping data and methods into a single unit (class). It restricts direct access to some of the object's components and can prevent the accidental modification of data. In Python, encapsulation can be achieved using private and public access modifiers.
# Private members are not accessible from outside the class, while public members are accessible from outside the class.
# Private members are defined using a single underscore (_) or double underscore (__). Public members are defined without any underscore.


# Practice...
# create account class with 2 attributes: balance & account no.
# create methods for debit, credit, and printing the balance.


class Account: 
    def __init__(self, acc, bal):
        self.account_no = acc 
        self.balance = bal
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}")
    #credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")    

    #print balance method
    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")    

acc1 = Account("123456789", 1000) # object creation
acc1.debit(200) # Output: Debited 200. New balance: 800
acc1.credit(500) # Output: Credited 500. New balance: 1300
acc1.print_balance() # Output: Account No: 123456789, Balance: 1300