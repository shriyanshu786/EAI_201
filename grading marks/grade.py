class Student:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def total(self):
        return self.math + self.science + self.english


students = []

for i in range(3):
    name = input("Enter name of student " + str(i+1) + ": ")

    # Math marks
    while True:
        try:
            math = int(input("Enter marks in Math (0-100): "))
            if math >= 0 and math <= 100:
                break
            else:
                print("Please enter between 0 to 100")
        except:
            print("Invalid number")

    # Science marks
    while True:
        try:
            science = int(input("Enter marks in Science (0-100): "))
            if science >= 0 and science <= 100:
                break
            else:
                print("Please enter between 0 to 100")
        except:
            print("Invalid number")

    # English marks
    while True:
        try:
            english = int(input("Enter marks in English (0-100): "))
            if english >= 0 and english <= 100:
                break
            else:
                print("Please enter between 0 to 100")
        except:
            print("Invalid number")

    # add student to list
    s = Student(name, math, science, english)
    students.append(s)

# print details
for s in students:
    print("Student:", s.name)
    print("Math:", s.math, "Science:", s.science, "English:", s.english)
    print("Total:", s.total())
    print("----------")

# find topper
topper = students[0]
for s in students:
    if s.total() > topper.total():
        topper = s

print("Topper is", topper.name, "with total", topper.total())
