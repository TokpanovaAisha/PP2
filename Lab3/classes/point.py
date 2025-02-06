import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("The coordinates of the point is: ", self.x ,"and", self.y)
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self, second_point):
        print("distance between 2 points is", math.sqrt((second_point.x - self.x)**2 + (second_point.y - self.y)**2))


point1 = Point(2, 3)
point2 = Point(1,3)
point1.show()
point2.show()
point1.move(4, 5)
point1.show()
point1.dist(point2)
