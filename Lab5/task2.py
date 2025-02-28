# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


import re

def find_ab(string):
    pattern = r"^ab{2,3}$"
    x = re.fullmatch(pattern, string)

    if x:
        return True
    else:
        return False

string = input("Enter the string: ")

if find_ab(string):
    print("Your string matches the pattern")
else:
    print("Your string doesn't match the pattern")
