
nums = (1,2,4,9,16,25,36,49,64,81,100,36,10,15,36,57,85,36)
x =36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print(x,"found at index",i)
    else:
        print("finding..")
    i += 1    