# 1. Write a Python program to subtract five days from current date.


import datetime

def subtract():
    
    current_date = datetime.datetime.now()
    days_5 = datetime.timedelta(days = 5)
    past = (current_date - days_5).strftime("%Y, %B, %d")
    
    return past

print(subtract())