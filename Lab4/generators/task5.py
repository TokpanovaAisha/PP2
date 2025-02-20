# 5. Implement a generator that returns all numbers from (n) down to 0.

def allnum(num):
    for i in range (num, -1, -1):
        yield i
        

num = int(input("Enter the number n: "))

for i in allnum(num):
    print(i)