with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")  # split the data by comma
    count = 0  # initialize count for even numbers
    for val in nums:
        try:
            if int(val.strip()) % 2 == 0:  # check if the number is even
                count += 1  # increment the count for even numbers
        except ValueError:
            print(f"Skipping invalid number: {val.strip()}")  # handle non-numeric values gracefully
    print("Count of even numbers:", count)  # print 