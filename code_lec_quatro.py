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

student = {
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
