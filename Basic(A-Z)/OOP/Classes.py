# Class is blueprint of creating new objects
# Object: instance of a class

# Class: Human
# Objects: Omar, Faruk, Danish

class PyPoint:
    def draw(self):
        print("draw")


point = PyPoint()
print(type(point))
print(isinstance(point, PyPoint))
