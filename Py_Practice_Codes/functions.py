def demo_functions():
    """Define and use functions with default arguments and multiple returns."""
    def power(base, exponent=2):
        return base ** exponent

    def stats(numbers):
        return min(numbers), max(numbers), sum(numbers)/len(numbers)

    print("2^3 =", power(2, 3))
    print("3^2 (default) =", power(3))
    data = [10, 20, 30, 40]
    mn, mx, avg = stats(data)
    print(f"Stats of {data}: min={mn}, max={mx}, avg={avg:.2f}")

demo_functions()