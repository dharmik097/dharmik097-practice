marks = [94.5, 87.5,97.5, 99.5, 96.5]
print(marks)
print(type(marks))
print(marks[0])

print(marks.sort())
print(marks.sort(reverse = True))
print(marks)
# --------------------------------------------------

movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# 2d method

movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))
print(movies)

# ---------------------------------------------------

list = []
list.append(input("enter ccomponents of list: "))
list.append(input("enter ccomponents of list: "))
list.append(input("enter ccomponents of list: "))
list.append(input("enter ccomponents of list: "))
list.append(input("enter ccomponents of list: "))

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("not palindrome")   
# -----------------------------------------------------------

students = ["c","c","D","A","A","B","B","A"]
students.sort()
print(students)


