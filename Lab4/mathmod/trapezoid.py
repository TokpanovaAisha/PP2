# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5


def areaTrap():
    height = int(input("Height: "))
    firstbase = int(input("Base, first value: "))
    secondbase = int(input("Base, second value: "))
    midline = (firstbase + secondbase) / 2
    area = midline * height
    
    return f'Expected Output: {area:.1f}'

print(areaTrap())