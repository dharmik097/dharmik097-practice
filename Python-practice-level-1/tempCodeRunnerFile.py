class Student:
    def __init__(self, name, marks1, marks2, marks3):       
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def calculate_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

s1 = Student("Arjun", 99, 98, 100)
print(s1.name, s1.marks1, s1.marks2, s1.marks3)
print("Average Marks:", s1.calculate_average())
# Output: Average Marks: 98.66666666666667