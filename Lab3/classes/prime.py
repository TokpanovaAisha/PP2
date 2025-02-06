# Write a program which can filter prime numbers in a list by using filter function. 
# Note: Use lambda to define anonymous functions.


class ListP():
    def __init__(self, numbers):
        self.numbers = numbers
        
    def isprime(self, number):
        if number < 2:
            return False
        for i in range (2, int(number * 0.5 + 1)):
            if number % i == 0:
                return False
        return True     
    
    def filterP(self):
        return list(filter(lambda x: self.isprime(x), self.numbers))
    
numbers = [1, 2, 50, 78, 17, 61, 78, 23, 7]

myList = ListP(numbers)
print(myList.filterP())