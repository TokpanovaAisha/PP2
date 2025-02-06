def volume (radius):
    V = 4/3 * 3.14 * pow(radius, 3)
    print("The volume of the sphere: ", V)

rad = int(input("Enter rhe radius: "))
volume(rad)