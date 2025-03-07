# Write a Python program to count the number of lines in a text file.

import os

file = open(r"C:\Users\Aisha\Desktop\pp2\Lab6\dir-and-files\for4task.txt")
count = 0
for lines in file:
    count += 1
print(f"File has {count} lines")