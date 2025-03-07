# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.


import os

file = (r"C:\\Users\\Aisha\\Desktop\\pp2\\Lab6\\dir-and-files\\delete_file.txt")

if os.path.exists(file):
    os.remove(file)
    print("The file was deleted")
else:
    print("There is no such file")