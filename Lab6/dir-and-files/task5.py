# Write a Python program to write a list to a file.

import os

file = open(r"C:\Users\Aisha\Desktop\pp2\Lab6\dir-and-files\for5task.txt", "a")
list = ["Hello world ", "I am 17 ", "Aisha ", "hello ", "12345 "]
for i in list:
    file.write(i)