# 1. Create a generator that generates the squares of numbers up to some number N.

def squareofnum():
    num = int(input("Enter the number: "))
    gen = (i ** 2 for i in range(num))

    for i in range(num):
        print(next(gen))
        
squareofnum()