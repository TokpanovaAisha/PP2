# Write a Python program to convert a given camel case string to snake case.

import re

def camel_snake(str1):
    pattern = r"(\w)(?=[A-Z])"
    str1 = re.sub(pattern, r"\1_", str1)
    str1 = str1.lower()
    print(str1)

string = input("Enter the string: ")
camel_snake(string)