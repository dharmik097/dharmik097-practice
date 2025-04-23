#loops
#2 types while and for
 
count = 9
while count <= 10 :
    print("hello")
    count += 5


#PRINT NUMBERS 1 TO 5
i = 1
while i <= 5:
    print(i)
    i += 1

#reverse
i = 5
while i >= 1:
    print(i)
    i -= 1
#PRACTICE

#PRINT NUMBER FROM 1 TO 100
 
i = 1
while i <= 100:
    print(i)
    i += 1

#print number 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1

#print multiplication table of number n
i = 1
n = int(input("put your value :"))
while i <= 10:
    print(n*i)
    i += 1


#print squre of the numbers

i = 1
while i <= 10:
    print(i*i)
    i += 1 

# print the elements of the following list using loop; [1,4,9,16, 25,36,49,64,81,100]

squres = [2,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(squres):
    print(squres[idx])
    idx += 1
