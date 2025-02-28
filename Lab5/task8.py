# Write a Python program to split a string at uppercase letters.
import re

def split_up_case(string):
    pattern = r"[A-Z][a-z]*"
    print(re.findall(pattern, string))

string = input("Enter the string: ")
split_up_case(string)