
class Account: 
    def __init__(self, acc, bal):
        self.account_no = acc 
        self.balance = bal
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}")
    #credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")    

    #print balance method
    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")    

acc1 = Account("123456789", 1000) # object creation
acc1.debit(200) # Output: Debited 200. New balance: 800
acc1.credit(500) # Output: Credited 500. New balance: 1300
acc1.print_balance() # Output: Account No: 123456789, Balance: 1300