import sys
from cs50 import get_int

numbers = [4, 6, 8, 2, 7, 5, 0]

sort = get_int("Sort: ")

if sort in numbers:
    print("Found")
else:
    print("Not found")