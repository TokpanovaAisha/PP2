class my_class():
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input("Enter the string: ")
    def printString(self):
        print(self.str.upper())

strx = my_class()

strx.getString()
strx.printString()