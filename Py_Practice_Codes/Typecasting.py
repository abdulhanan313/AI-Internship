def demo_typecasting():
    """Implicit and explicit type conversion."""
    num_int = 10
    num_float = 3.14
    result = num_int + num_float       # implicit: int → float
    print("Implicit:", result, type(result))