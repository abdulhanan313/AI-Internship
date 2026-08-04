def students(name, **args):
    print(f"Name: {name}")
    for key, values in args.items():
        print(f"{key}:{values}")





print(students("Honey", age=20, grade="A", major="Computer Science"))
print(students("Ahmad", age=22, grade="B", major="Medical", hobbies=["Reading", "Swimming"]))
