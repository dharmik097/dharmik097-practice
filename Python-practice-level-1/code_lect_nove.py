# OOPS part 2       

# del keyword
# The del keyword is used to delete an object or an attribute of an object. It can be used to free up memory that is no longer needed.


class Student:
    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable  
 


s1 = Student("John Doe", 20) # object creation

s2 = Student("Jane Smith", 22) # object creation

del s1 # delete object s1   
print(s1.name, s1.age) # Output: John Doe 20        
print(s2.name, s2.age) # Output: Jane Smith 22


#Private(like) attributes & methods 
# Private attributes and methods are those that cannot be accessed from outside the class. They are defined using a single underscore (_) before the attribute or method name.
# Private attributes and methods are used to hide the implementation details of a class and to prevent accidental modification of the attributes or methods from outside the class.
# Private attributes and methods can only be accessed from within the class. They are not accessible from outside the class.
# Private attributes and methods are not truly private in Python, but they are a convention to indicate that they should not be accessed from outside the class.
# Private attributes and methods are defined using a single underscore (_) before the attribute or method name.



class Student:      
    def __init__(self, name, age): # constructor
        self._name = name # private instance variable
        self._age = age # private instance variable  
 
    def _welcome(self): # private method
        print("Welcome to the class!")          


s1 = Student("John Doe", 20) # object creation
s2 = Student("Jane Smith", 22) # object creation
s1._welcome() # Output: Welcome to the class!       


# Inheritance
# Inheritance is a mechanism in Python that allows a class to inherit attributes and methods from another class. The class that inherits is called the child class, and the class that is inherited from is called the parent class.
# Inheritance allows for code reusability and helps to create a hierarchical structure in the code.
# Inheritance is a powerful feature of OOP that allows for code reusability and helps to create a hierarchical structure in the code.


class Car:
    @staticmethod
    def start():
        print("car started!")

    @staticmethod
    def stop():
        print("car stopped!")

class ToyotaCar(Car): # child class
    def __init__(self, brand):
        self.name = brand


class Fortuner(ToyotaCar): # child class of ToyotaCar
    def __init__(self, brand):
        self.type = type       

# car1 = ToyotaCar("Fortuner") # object creation
# car2 = ToyotaCar("Innova")  # object creation  
car1 = Fortuner("diesel") # object creation
car1.start()


print(car1.name) # Output: Fortuner
print(car2.name) # Output: Innova

print(car1.start()) # Output: car started!
print(car2.stop()) # Output: car stopped!
print(car1.color) # Output: black


# Types of Inheritance
# There are several types of inheritance in Python, including single inheritance, multiple inheritance, multilevel inheritance, and hierarchical inheritance. 

#multiple inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B" 

class C(A, B): # child class of A and B
    varC = "welcome to class C"

c1 = C() # object creation
print(c1.varA) # Output: welcome to class A
print(c1.varB) # Output: welcome to class B
print(c1.varC) # Output: welcome to class C

#super meathod
# The super() method is used to call a method from the parent class. It is used to access the parent class's methods 
# and attributes from the child class. The super() method returns a temporary object of the parent class that 
# allows access to its methods and attributes.   

class Car:
    def __init__(self, type):
        self.type = type  # Define the 'type' attribute
    @staticmethod
    def start():
        print("car started!")

    @staticmethod
    def stop():
        print("car stopped!")

class ToyotaCar(Car): # child class
    def __init__(self, name, type): #here type is not
        self.name = name
        super().__init__(type) # call parent class constructor
        # self.type = type


car1 = ToyotaCar("Fortuner", "electric") # object creation 
print(car1.type) # Output: electric



# class method
# Class methods are methods that are bound to the class and not the instance of the class. They can be called on the class itself, rather than on an instance of the class. 

class Person:
    name = "anonymous" # class variable
    
    def changeName(self, name):
        Person.name = name # class method, focus here Person.name not self.name

p1 = Person() # object creation
p1.changeName("Vikrant Patel") # call class method
print(p1.name) # Output: Vikrant Patel
print(Person.name)  # Output: Vikrant Patel both gives same output but if we use self.name then it will give annonymous


#USE OF CLASS METHOD IN ABOVE EXAMPLE
class Person:
    name = "anonymous" # class variable
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person() # object creation
p1.changeName("Vikrant Patel") # call class method
print(p1.name) # Output: Vikrant Patel
print(Person.name)  # Output: Vikrant Patel both gives same output.
 


 #property decorator
# The property decorator is used to create properties in Python. Properties are a way to define methods that can be accessed like attributes.
# Properties allow for encapsulation and data hiding, as they can be used to control access to the attributes of a class.   


class Student:
    def __init__(self, phy, chem, math): # constructor
        self.phy = phy # private instance variable
        self.chem = chem
        self.math = math        

    @property
    def percentage(self): # property method
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
St1 = Student(90, 80, 70) # object creation
print(St1.percentage) # Output: 80.0%
         
#change any marks
St1.phy = 100 # change phy marks
print(St1.percentage) # Output: 83.33%

#----


class Complex:
    def __init__(self, real, img): # constructor
        self.real = real # instance variable
        self.img = img # instance variable

    def showNumber(self): # method to show complex number
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        nreReal = self.real + num2.real # add real part
        newImg = self.img + num2.img # add img part
        return Complex(nreReal, newImg)
    
    def __sub__(self, num2):
        nreReal = self.real - num2.real
        newImg = self.img - num2.img    
        return Complex(nreReal, newImg)
    
    
num1 = Complex(2, 3) # object creation
num2 = Complex(4, 5) # object creation
num3 = num1 + num2 # add two complex numbers
num4 = num1 - num2 # subtract two complex numbers

num1.showNumber() # Output: 2 i + 3 j   
num2.showNumber() # Output: 4 i + 5 j
num3.showNumber() # Output: 6 i + 8 j
num4.showNumber() # Output: -2 i + -2 j


#practice question
# 1. Define a Circle class to create circle with radius r using the constructor.
# Define an Area() method to calculate the area of the circle.
# Define a Perimeter() method to calculate the circumference of the circle.


class Circle:
    def __init__(self, radius): # constructor
        self.radius = radius # instance variable

    def Area(self): # method to calculate area of circle
        return 3.14 * self.radius * self.radius
    
    def Perimeter(self): # method to calculate perimeter of circle
        return 2 * 3.14 * self.radius
    



circle1 = Circle(5) # object creation
print("Area of circle is:", circle1.Area()) # Output: Area of circle is: 78.5
print("Perimeter of circle is:", circle1.Perimeter()) # Output: Perimeter of circle is: 31.4            




#qn2
# Define a class Employee class with attributes role, department, and salary. this class also showDetails() method.
# Create an Engineer class that inherits properties form Employee & has additioal attributes : name and age.






class Employee:
    def __init__ (self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self): # method to show details of employee
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)


class Engineer(Employee): # child class of Employee
    def __init__(self, name, age): # constructor
        self.name = name # instance variable
        self.age = age # instance variable
        super().__init__("Engineer", "IT", "75000") # call parent class constructor



e1 = Employee("Engineer", "IT", 50000) # object creation
e2 = Employee("Manager", "HR", 60000) # object creation

e1.showDetails() # Output: Role: Engineer Department: IT Salary: 50000
engg1 = Engineer("John Doe", 25) # object creation
engg1.showDetails() # Output: Role: Engineer Department: IT Salary: 75000




#qn3
#Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that:  order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self, item, price): # constructor
        self.item = item # instance variable
        self.price = price # instance variable
    
    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("Laptop", 50000) # object creation
order2 = Order("Mobile", 30000) # object creation

print(order1 > order2) # Output: True
print(order2 > order1) # Output: False


