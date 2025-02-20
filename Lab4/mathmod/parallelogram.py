# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

def parallelogram_area():
    base = int(input("Length of base: "))
    height = int(input("Height of parallelogram: "))
    area = base * height
    
    return print(f"Area of parallelogram is: {area:.1f}")

parallelogram_area()