def demo_loops():
    """Nested loops and break/continue."""
    # For loop with enumerate
    for i, char in enumerate("Python"):
        if i == 3:
            continue    # skip 'h'
        print(f"Index {i}: {char}")

    # While loop with break
    n = 0
    while n < 10:
        n += 1
        if n == 5:
            break
        print(n, end=" ")
    print()

    # Nested loops – multiplication table
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i}×{j}={i*j:2d}", end="  ")
        print()


demo_loops()