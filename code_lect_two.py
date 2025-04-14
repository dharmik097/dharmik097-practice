str1 = "Jay"
str2 = "Hind"
Final_str = str1+ '' + str2
print(Final_str)
lenfinal = len(Final_str)
print(lenfinal)
print(Final_str[0:5] )
print(Final_str[-5:-2] )


A = input("first name :")
print(len(A))

str = "sjdfhu$$bjk4$j4$jJ$j$kj4j$jJ$"
print(str.count("$"))


age = int(input("write your age - "))
if (age >= 18):
    print("can vote and apply for DL")

elif(age<=18):
    print("can not drive car")    

marks = int(input("write the marks -"))

if(marks>= 90):
    print("grade A")
elif(marks >= 80):
    print("grade B")  
elif(marks >= 70):
    print("grade c")
elif(marks <= 70):
    print("grade D")        

marks = int(input("write the marks -"))
if(marks>= 90):
    grade = 'A'
elif(marks >= 80):
    grade = 'B' 
elif(marks >= 70):
    grade = 'C'
elif(marks <= 70):
    grade = 'D'        
    
print("grade of student ->", grade)
# ________________________________________________________________________________

num = int(input("enter number:"))
rem = num % 2
if (rem == 0):
    print("EVEN")
else:
    print("ODD")    
# ________________________________________________________________________________

A = int(input("enter number a:"))
B = int(input("enter number b:"))
C = int(input("enter number c:"))
D = int(input("enter number d:"))


if ( A > B and A > C and A > D):
    ans = A
elif ( B > A and B > C and B > D):
    ans = B
elif ( C > B and C > A and C > D):
    ans = C
elif ( D > B and D > A and D > C):
    ans = D

print("greatest number is :",ans)
# ________________________________________________________________________________

# num is multple of 7 or not

num = int(input("enter number:"))
rem = num % 7

if(rem==0):
    print("yes this number is multiple of 7")
else:
    print("no this number is not multiple of 7")
    