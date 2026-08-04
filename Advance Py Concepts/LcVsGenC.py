import sys
from timeit import timeit

# 1. Memory Size Comparison (Use sys.getsizeof directly)
lc = [i for i in range(1000)]
gen = (i for i in range(1000))

print(lc[33])
print(lc.append(24))

#while generators dont have above capabilities



#print(f"List comprehension size: {sys.getsizeof(lc)} bytes")
#print(f"Generator expression size: {sys.getsizeof(gen)} bytes")

# 2. Execution Time Comparison (Pass statements as strings or functions)
#list_time = timeit("[i for i in range(1000)]", number=10000)
#gen_time = timeit("(i for i in range(1000))", number=10000)



#print(f"List creation time: {list_time:.5f} seconds")
#print(f"Generator creation time: {gen_time:.5f} seconds")
