class Teacher:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y}")


point = Teacher(1, 2)
print(point.default_color)
point.draw()


another = Teacher(3, 4)
another.draw()
