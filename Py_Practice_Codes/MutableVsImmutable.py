def demo_mutable_immutable():
    """Immutable: int, str, tuple. Mutable: list, dict, set."""
    # Immutable – reassignment creates new object
    a = 10
    print("id(a) before:", id(a))
    a += 5
    print("id(a) after:", id(a))  # different

    # Mutable – modify in place
    lst = [1, 2, 3]
    print("id(lst) before:", id(lst))
    lst.append(4)
    print("id(lst) after:", id(lst))  # same

    # Tuple (immutable) – cannot change elements
    t = (1, 2, 3)
    # t[0] = 5   # TypeError

demo_mutable_immutable()