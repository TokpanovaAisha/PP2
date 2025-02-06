def ispalindrome(str):
    reversedstr = str[ : : -1]
    if reversedstr == str:
        print("Yes, it is palindrome!")
    else:
        print("No, it is not palindrome!")

word = input("Enter the word or phrase: ")
ispalindrome(word)