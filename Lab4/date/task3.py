# 3. Write a Python program to drop microseconds from datetime.


import datetime

def mcseconds():
    current = datetime.datetime.now()
    microsecs = current.replace(microsecond = 0)

    print(f"Current date and time: {current}")
    print(f"Current date and time with no microseconds: {microsecs}")
    
mcseconds()