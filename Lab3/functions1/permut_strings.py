from itertools import permutations

def permutat(str):
    p_list = permutations(str)
    for perm in p_list:
        print(''.join(perm))

str = input("Enter the string: ")
permutat(str)