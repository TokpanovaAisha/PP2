# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def a_b(string):

    pattern = r"^a.+b$"
    if re.fullmatch(pattern, string):
        print("Your string matches the pattern")
    else:
        print("Your string doesn't match the pattern")

string = input("Enter the string: ")
a_b(string)
