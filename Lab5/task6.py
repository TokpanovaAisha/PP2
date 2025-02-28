# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

def colon(string):
    pattern = r"[, .]"
    print(re.sub(pattern, ":", string))


string = input("Enter the string: ")
colon(string)