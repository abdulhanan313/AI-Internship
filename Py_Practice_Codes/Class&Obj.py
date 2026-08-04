class Car:
    """Simple class with attributes and a method."""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        return f"{self.brand} {self.model} ({self.year})"

def demo_classes_objects():
    my_car = Car("Toyota", "Corolla", 2020)
    print("Car:", my_car.description())

demo_classes_objects()