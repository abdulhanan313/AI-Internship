class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def create_anonymous(cls, age):
        return cls("Anonymous", age)   # alternative constructor

def demo_class_method():
    print("Species:", Person.get_species())
    anon = Person.create_anonymous(25)
    print(f"Anonymous: {anon.name}, age {anon.age}")


demo_class_method()