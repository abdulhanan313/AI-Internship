

class Library:
    def __init__(self,name):
        self.name = name
    



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("The blue whale", "Nicholas Sparks")
l1 = Library("NY Library")
l2 = Library("LA Library")

print()
print(l1)