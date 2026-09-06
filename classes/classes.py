class Point:
    default_color = "red"  # Class Attributes

    def __init__(self, x, y):
        self.x = x  # Instance Sttributes
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x} , {self.y})"

    def draw(self):
        print(f"draw {self.x} {self.y}")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 3)
point.z = 10
print(type(point))
print(isinstance(point, int))
point.draw()
point.default_color = "blue"

print(point.default_color)

point2 = Point(6, 6)

print(point2.default_color)

Point.default_color = "black"

zero = Point.zero()
zero.draw()

print(point)

point_a = Point(1, 2)
point_b = Point(1, 2)

print(point_a == point_b)


print(point_a > point_b)
print(point_a + point_b)
