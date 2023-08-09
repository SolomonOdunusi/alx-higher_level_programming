#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10
if last_num > 5:
    comp_num = "greater than 5"
elif last_num == 0:
    comp_num = "0"
else:
    comp_num = "less than 6 and not 0"
print(f"Last digit of {number} is {last_num} and is {comp_num}")
