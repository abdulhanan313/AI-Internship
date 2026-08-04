nums = [1,2,3,4,5,6,7,8,9,10]
print("by filter and map")
even = list(filter(lambda x:x%2==0,nums))
print(even)
sqr = list(map(lambda x:x**2,even))
print(sqr)

print("by list Comprehension")

Even = [x for x in nums if x%2==0]
print(Even)
Sqr = [x**2 for x in Even]
print (Sqr)