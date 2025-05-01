
class Order:
    def __init__(self, item, price): # constructor
        self.item = item # instance variable
        self.price = price # instance variable
    
    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("Laptop", 50000) # object creation
order2 = Order("Mobile", 30000) # object creation

print(order1 > order2) # Output: True
print(order2 > order1) # Output: False