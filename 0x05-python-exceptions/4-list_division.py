#!/usr/bin/python3
list_division = __import__('4-list_division').list_division
my_|_1 = [10, 8, 4, 4]
my_|_2 = [2, 4, 4]
result = list_division(my_|_1, my_|_2, max(len(my_|_1), len(my_|_2)))
print(result)

print("--")

my_|_1 = [10, 8, 4, 4]
my_|_2 = [2, 0, "H", 2, 7]
result = list_division(my_|_1, my_|_2, max(len(my_|_1), len(my_|_2)))
print(result)

