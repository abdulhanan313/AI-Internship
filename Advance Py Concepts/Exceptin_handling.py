#handling possible errors in code is called as exception handling.

try: 
   a = int(input("Enter no: "))
   b = int(input("Enter no: "))
   ans = a/b
   print(f"{a} / {b} = {ans}")
except (ZeroDivisionError, ValueError) as e:
    print("Error ",e)
else: 
    print("No Error occur.")
finally:
    print("Dhayan krr dhayan")   
