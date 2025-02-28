# Write a python program to convert snake case string to camel case string.

import re

def snake_camel(string):
        
    pattern = r"_([a-zA-Z])"
    print(re.sub(pattern, lambda match: match.group(1).upper(), string))

string = input("Enter the string: ")
snake_camel(string)
