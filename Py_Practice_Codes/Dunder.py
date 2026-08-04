class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def demo_magic_methods():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    v4 = v2 - v1
    print(f"{v1} + {v2} = {v3}")
    print(f"{v2} - {v1} = {v4}")
    print(f"v1 == v2? {v1 == v2}")

demo_magic_methods()