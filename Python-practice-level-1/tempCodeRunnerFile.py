n = int(input("factorial of first n numbers where n ="))
fact = 1
i = 1
while i <= n:
    fact *= i 
    i += 1

print("factorial =", fact)
