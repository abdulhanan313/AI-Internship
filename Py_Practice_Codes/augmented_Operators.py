def demo_augmented_assign():
    """Using +=, -=, *=, /=, etc."""
    x = 5
    x += 3   # equivalent to x = x + 3
    x *= 2
    x /= 4
    print(f"Augmented result: {x}")  # 4.0

    # With lists (mutability)
    lst = [1, 2]
    lst += [3, 4]   # extends list in place
    print("List after +=:", lst)

demo_augmented_assign()



