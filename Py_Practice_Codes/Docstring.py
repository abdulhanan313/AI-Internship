def demo_docstring():
    """This function demonstrates the use of docstrings.
    
    Docstrings are string literals that appear as the first statement
    in a module, function, class, or method. They are used for documentation.
    You can access them via .__doc__ or help().
    """
    print("Docstring of this function:")
    print(demo_docstring.__doc__)

demo_docstring()