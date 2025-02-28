# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def underscore(string):
    
    pattern = r"^[a-z]+(?:_[a-z]+)+$"
    x = re.fullmatch(pattern, string)

    if x:
        return True
    else:
        return False

string = input("Enter the string: ")

if underscore(string):
    print("Your string matches the pattern")
else:
    print("Your string doesn't match the pattern")
