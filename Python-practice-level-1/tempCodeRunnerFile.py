
import random
import string

pass_length = int(input("Enter the length of the password: "))
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=pass_length))

print("Generated password:", password)