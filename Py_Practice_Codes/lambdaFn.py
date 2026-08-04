#Use of lambda function to sort a list of tuples based on the first and second elements of the tuple.
students = [("John", 25), ("Alice", 22), ("Bob", 30), ("Eve", 28)]

students.sort(key=lambda std:std[0])
print(students)    #sorted by name

by_age = sorted(students, key=lambda std:std[1])

print(by_age)      #sorted by age
