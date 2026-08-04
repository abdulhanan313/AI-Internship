from functools import reduce
nums = [1,2,3,4,5,6,7]
product = reduce(lambda a,b:a*b,nums)
print(product)  



sum = reduce(lambda a,b:a+b,nums)
print(sum)
#a reduce fn is used for