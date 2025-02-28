# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
def up_low(string):

    pattern = r"^[A-Z].[a-z]+$"

    if re.fullmatch(pattern, string):
        print("Your string matches the pattern")
    else:
        print("Your string doesn't match the pattern")


string = input("Enter the string: ")
up_low(string)
