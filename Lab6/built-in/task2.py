# Write a Python program with builtin function that accepts 
# a string and calculate the number of upper case letters and lower case letters

str1 = str(input("Enter the string: "))
lower = 0
upper = 0
for char in str1:
    if(char.islower()):
        low += 1
    else:
        up +=1

print(low, up)