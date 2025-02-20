# 2. Write a program using generator to print the even numbers between 0 and n in 
# comma separated form where n is input from console.

def even(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield i
            
num = int(input("Enter the number: "))
print(", ".join(map(str, even(num))))   