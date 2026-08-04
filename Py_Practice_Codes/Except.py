def demo_try_except():
    """Handle division by zero and file not found."""
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    finally:
        print("Execution of try-except complete.")

demo_try_except()