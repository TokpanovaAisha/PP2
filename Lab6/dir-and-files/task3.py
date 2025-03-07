# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.

import os

path = 'C:\\Users\\Aisha\\Desktop\\pp2' 

def check(path):
    if os.path.exists(path):
        print("The path exists.")
        file = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Name of file:", file)
        print("Directory:", directory)
    else:
        print("The path does not exist.")

check(path)