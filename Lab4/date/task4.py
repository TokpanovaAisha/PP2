# 4. Write a Python program to calculate two date difference in seconds.

import datetime

def difference():
    today = datetime.datetime.now()
    d = datetime.datetime(2025, 2, 12)
    difference = abs(int((today - d).total_seconds()))

    return print(f"{difference} second passed from 12 february ")

difference()