#raise in exception handling is used to raise an exception when a certain condition is met. In this example, we define a function `check_age` that raises a `ValueError` if the age provided is less than 18.
def check_age(age):
   if(age<18):
       raise ValueError(f" {age} Age is less than 18.")
   return age


print("Age is ",check_age(20))
try:
   print(check_age(8))
except ValueError as e:
    print("Error ",e)