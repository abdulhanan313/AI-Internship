def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end-start:.4f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(0.1)
    return "Done"

def demo_decorator():
    print(slow_function())

demo_decorator()
