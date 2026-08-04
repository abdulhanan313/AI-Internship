def demo_lambda():
    """Using lambda with map, filter, sorted."""
    nums = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    words = ["apple", "banana", "cherry", "date"]
    sorted_by_len = sorted(words, key=lambda w: len(w))
    print("Squares:", squares)
    print("Evens:", evens)
    print("Sorted by length:", sorted_by_len)

#demo_lambda()

add  = lambda a,b: a+b+10

print(add(5, 3))