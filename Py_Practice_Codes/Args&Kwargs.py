def demo_args_kwargs():
    def print_args(*args, **kwargs):
        print("Positional args:", args)
        print("Keyword args:", kwargs)

    print_args(1, 2, 3, name="Alice", age=30)

    # Unpacking
    numbers = [4, 5, 6]
    print_args(*numbers, city="NYC")

demo_args_kwargs()