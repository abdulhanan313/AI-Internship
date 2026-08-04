from functools import reduce  
words = ["hi", "hello", "world", "python", "programming"]

Red_Words = reduce(lambda x,y : x if len(x) > len(y) else y,words)
print (Red_Words)