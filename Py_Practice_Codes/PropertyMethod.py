class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

def demo_property():
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")
    temp.celsius = 30
    print(f"New Celsius: {temp.celsius}°C")

demo_property()