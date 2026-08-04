class student:
    
    count = 0
    total_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count +=1
        student.total_age += age

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} is {self.age}"
        

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    @classmethod
    def get_average_age(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average age of students: {cls.total_age / cls.count}"
    
student1 = student("John", 20)
student2 = student("Jane", 22)
student3 = student("Jim", 21)

print(student.get_count())
print(student.get_average_age())
