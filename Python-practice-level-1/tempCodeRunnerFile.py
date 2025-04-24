squares = (1,4,9,16,25,36,49,64,81,100)
x = int(input("number : "))
idx = 0
for nums in squares:
    if(nums == x):
        print( "found at idx", idx )
        break
    idx += 1
