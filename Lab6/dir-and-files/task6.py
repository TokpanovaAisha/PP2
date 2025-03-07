# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def generate_A_to_Z():
    for i in string.ascii_uppercase:
        filen = i + '.txt'
        with open(filen, 'w') as file:
            file.write(f"File: {filen}\n")
        print(f"File {filen} has been created.")

generate_A_to_Z()