#Functions
#Block of statement that performs a specific task
#Function is a reusable piece of code that can be called when needed

#function definition
def calc_sum(a, b): #a and b are parameters.
    sum = a + b
    print("The sum of a and b is :", sum)
    return sum

#Function call
calc_sum(1,2) # 1 and 2 are arguments.
calc_sum(3,4)
calc_sum(5,6)
calc_sum(7,8)


def print_hello():
    print("Hello World!")
print_hello()
print_hello()
print_hello()          

#ex2
def calc_avg(a,b,c):
    avg = (a+b+c)/3
    print("The average of a, b and c is :", avg)
    return avg #➡️ This gives the average back to the program that called calc_avg, so you can save it or use it.

calc_avg(1,2,3)

#some basics
print("jay", end=" ") #end is used to print in the same line
print("Hind") #default is \n, so it will print in the next line
print("Hello", "World", sep="*") #sep is used to separate the strings with a specific character. Default is space.  

#default arguments
def calc_prod(a=1, b=2): #b is a default argument. If not provided, it will take the default value of 2.
    prod = a * b
    print("The product of a and b is :", prod)      
    return sum

calc_prod(3,4) # 3 and 4 are arguments.

#####practice
#WAF to print the length of the list.(list is the parameter).

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
heroes = ["Dharam", "Karana", "Arjun", "ironman", "thor"]   

def print_Len(list): #list is the parameter.
    length = len(list) #len is a built-in function to find the length of the list.
    print("The length of the list is :", length)
    return length

print_Len(cities) #cities is the argument.
print_Len(heroes) #heroes is the argument.

#WAFto print the elements of the list in a single line(list is the parameter).
def print_list(list): #list is the parameter.
    for i in list: #i is the element of the list.
        print(i, end=" ") #end is used to print in the same line.
         
    # print("The elements of the list are :", list)


print_list(cities) #cities is the argument.     
print_list(heroes) #heroes is the argument.  


# WAF to find the factorial of n (n is the parameter).

def calc_factorial(n): #n is the parameter.
    fact = 1 #fact is the variable to store the factorial.
    for i in range(1, n+1): #i is the variable to iterate from 1 to n.
        fact = fact * i #fact is the product of all the numbers from 1 to n.
    print("The factorial of", n, "is :", fact) #n is the argument.
    return fact 


calc_factorial(5) #5 is the argument.
calc_factorial(6) #6 is the argument.

# WAF to covert usd to inr (usd is the parameter).
def conv(usd_value):
    inr_value = usd_value * 83
    print("The value of", usd_value, "usd in inr is :", inr_value) #usd_value is the argument.
    return inr_value

conv(100) 

# recursion
# A function that calls itself is called a recursive function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# prints n  to 1 backwareds.
# WAF to print n to 1 backwards (n is the parameter).
def show(n): #n is the parameter.
    if (n == 0): #base case
        return
    print(n) #n is the argument.
    show(n-1) #recursive call

show(5) #5 is the argument.

#call stack
# A call stack is a data structure that stores information about the active subroutines of a computer program. 