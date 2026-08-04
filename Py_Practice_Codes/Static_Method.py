class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

def demo_static_method():
    print("Static add:", MathUtils.add(5, 3))
    print("Static multiply:", MathUtils.multiply(4, 2))


demo_static_method()