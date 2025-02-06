def solve(numheads, numlegs):
    rabbits = numlegs / 2 - numheads
    chickens = numheads - rabbits
    print ("Rabbits: ", rabbits) 
    print ("Chickens: ", chickens)

numheads = int(input("Enter number of heads: "))
numlegs = int(input("Enter number of legs: "))

solve(numheads, numlegs)  