
cities = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
heroes = ["Dharam", "Karana", "Arjun", "ironman", "thor"]   
def print_list(list, index): #list and index are the parameters.
    if (index == len(list)): #base case
        return
    print(list[index]) #list[index] is the argument.
    print_list(list, index+1) #recursive call
print_list(cities, 0)
print_list(heroes, 0) #heroes is the argument.