# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

str1 = input("Enter the strng: ")
rev_str1 = ''.join(reversed(str1))

if str1 == rev_str1:
    print("Yes, it is palindrome")
else:
    print("No, it is not palindrome")