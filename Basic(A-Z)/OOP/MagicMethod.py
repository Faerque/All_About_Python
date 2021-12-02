class Teacher:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Teacher({self.x}, {self.y}")


point = Teacher(1, 2)

print(str(point))
