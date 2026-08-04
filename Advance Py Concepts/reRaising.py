def check_age(age):
   if(age<18):
       raise ValueError(f" {age} Age is less than 18.")
   return age


print("Age is ",check_age(20))
try:
   print("Age is ",check_age(8))
except ValueError as e:
    print("Error ",e)
    raise  # re-raising the exception to propagate it further