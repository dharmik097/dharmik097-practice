def show(n): #n is the parameter.
    if (n == 0): #base case
        return
    print(n) #n is the argument.
    show(n-1) #recursive call

show(5) #5 is the argument.