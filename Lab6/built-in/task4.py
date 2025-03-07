# Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858

import math
import time

def square(num, ms):
    time.sleep(ms / 1000)
    r = math.sqrt(num)
    return r

num = int(input())
ms = int(input())
result = square(num, ms)
print(f"Square root of {num} after {ms} miliseconds is", result)