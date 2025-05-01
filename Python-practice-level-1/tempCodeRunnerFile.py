class Student:
    def __init__(self, phy, chem, math): # constructor
        self.phy = phy # private instance variable
        self.chem = chem
        self.math = math        

    @property
    def percentage(self): # property method
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
St1 = Student(90, 80, 70) # object creation
print(St1.percentage) # Output: 80.0%
         
#change any marks
St1.phy = 100 # change phy marks
print(St1.percentage) # Output: 83.33%
