#filter(fn,collection) is a high order function which takes a function and a collection as an argument. It applies the function to each item in the collection and returns a new collection with only those items for which the function returned True.

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

evens = list(filter(lambda x:x%2==0,nums))  #lambda in filter gives us only those items for which the condition is True. In this case, it will return only even numbers from the list.
print(evens)
