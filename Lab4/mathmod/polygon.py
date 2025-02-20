# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625


import math

def polygon_area():
    
    sides = int(input("Input number of sides: "))
    length = int(input("Input the length of a side: "))
    area = ((sides * pow(length, 2)) / 4) * (math.sin(math.pi / sides)/math.cos(math.pi / sides))
    
    return f'Area of your polygon is {area:.2f}'

print(polygon_area())