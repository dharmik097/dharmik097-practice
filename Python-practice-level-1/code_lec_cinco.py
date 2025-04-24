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


# ex-2

heros = ["Dharam","Ironman","Thor"]
idx = 0
while idx < len(heros):
    print(heros[idx])
    idx += 1


# search for a number x in this tuple using loop [2,4,9,16,25,36,49,64,81,100]

nums = (1,2,4,9,16,25,36,49,64,81,100,36,10,15,36,57,85,36)
x =36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print(x,"found at index",i)
    else:
        print("finding..")
    i += 1    

# uses of break and continue in loops.
i = 1 
while i <= 5:
    print(i)
    if(i == 3):
        break # it stops loop
    i += 1
print("end of loop")   

# ex2  SEE DIFFERENCE BETWEEN BOTH EXAMPLES
nums = (1,2,4,9,16,25,36,49,64,81,100,36,10,15,36,57,85,36)
x =36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print(x,"found at index",i)
        break
    else:
        print("finding..")
    i += 1    


# use of CONTINUE

i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# op 
1
3
5
7
9

i = 0
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

# op 
0
2
4
6
8
10
 

 --------------------------------------------------

# for loop

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

#ex2

tup = (1,2,3,4,5,6,7,8,9)

for num in tup:
    print(num)
 
 #exe 3

str = "Jay Hind"

for char in str:
    print(char)
else:
    print("End")    

#ex-4

str = "Jay Hind"

for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("End")   


#MORE PRACTICE QNS

squres = [1,4,9,16,25,36,49,64,81,100]

for nums in squres:
    print(nums)


              

