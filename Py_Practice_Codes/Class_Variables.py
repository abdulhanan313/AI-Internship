class Student:
    school = "MIT"          # class variable
    count = 0

    def __init__(self, name):
        self.name = name    # instance variable
        Student.count += 1

def demo_class_variables():
    s1 = Student("Alice")
    s2 = Student("Bob")
    print(f"School: {Student.school}")
    print(f"Students count: {Student.count}")
    print(f"{s1.name}'s school: {s1.school}")  # inherited


demo_class_variables()