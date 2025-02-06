# Define a class named Rectangle which inherits from Shape class from task 2. 
# Class instance can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.


class Shape():
    def __init__ (self, length, width):
        self.length = length
        self.width = width 

class Rectangle(Shape):
    def area(self):
        print(self.length * self.width)

a = int(input())
b = int(input())
S = Rectangle(a, b)
S.area()