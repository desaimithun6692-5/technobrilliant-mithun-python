class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"x co ordinate value : {self.x} y coordinate value : {self.y}")

    def calulate(self):
        print(self.x * self.y)


p1 = Point(10, 20)
p1.draw()
p1.calulate()
print(p1.x)

# rectangle 2 properties length and breadth , methods area and perimeter

# p2 = Point(20,90)
# print(p2.x)
