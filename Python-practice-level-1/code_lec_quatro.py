#dictionary
info = {
    
    "name" : "stallwarts",
    "subjects" : ["Python","C","Java","C#","R",],
    "learning" : "coading",
    "age" : 27,
    "is_adult" : True,
    "marks" : 95.5,
}

info["surname"] = "bhartiy"

print(info["name"])   #print specific key
info["name"] = "vikrant"  #for overwrite.

print(info) 

#nested dictionary -> dictionary inside the dictionary

student =  {
"name" : "Vikrant Patel",
"subjects" : {
"phy" : 97,
"chem" : 98, 
"math" : 99
} 
}




print(student["subjects"])

print(student["subjects"]["chem"]) #to get more specific information

print (student.keys())  #print keys of dict 

print (list(student.keys())) # to get in list using typecast


print(len(student)) # tof get leanghth of dict
print (len(list(student.keys()))) #to get length 

print(student.values()) #print values like this -> dict_values(['Vikrant Patel', {'phy': 97, 'chem': 98, 'math': 99}])
print (list(student.values())) #print list like this ['Vikrant Patel', {'phy': 97, 'chem': 98, 'math': 99}] here list ni andar dictionfary 6. to 1data type ni andar bijo dataype store karishakay chhe. 

print(student.items())# it returns all items of dictionary.
print(list(student.items())) # it gives list like this [('name', 'Vikrant Patel'), ('subjects', {'phy': 97, 'chem': 98, 'math': 99})]   
pairs = (list(student.items()))
print(pairs[0]) # can specific part of list.

print(student["name"])  #print name  but-> in case of error code after this will not run
print(student.get("name")) # same as above print name  ->but in case or error it will run remainig code 


print("before")
print(student["name1"]) #if some issue here it will show error beaus of wrong name here and will not run remaining code
print("after")


print("before")
print(student.get("name2"))  #it will run whole code except this line because of error of name only
print("after")

# output
#before
# None
# after
