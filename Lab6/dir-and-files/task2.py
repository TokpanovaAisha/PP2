# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os

path = 'C:\\Users\\Aisha\\Desktop\\pp2' 

mylist = os.listdir(path)

for i in mylist:
    full_path = os.path.join(path, i)
    print('Existence:', os.access(full_path, os.F_OK))
    print('Readability', os.access(full_path, os.R_OK))
    print('Writability:', os.access(full_path, os.W_OK))
    print('Executability:', os.access(full_path, os.X_OK))
    print()