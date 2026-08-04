#High Order: a fn in which you can pass another fn, collection as a parameter.
#Map Fn: in map fn we can pass a fn as a parameter to another function. This allows us to apply a function to each item in an iterable (like a list) and return a new iterable with the results.


nums = [1, 2, 3, 4, 5]

sqr = list(map(lambda x:x**2, nums)) #this will return a map object which is an iterable. To see the result we can convert it to a list.
print(sqr)
