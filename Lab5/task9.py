# Write a Python program to insert spaces between words starting with capital letters.

import re

def space_capital(string):
    pattern = r"(?=[A-Z])"
    print(re.sub(pattern, " ", string))

string = input("Enter the string: ")
space_capital(string)