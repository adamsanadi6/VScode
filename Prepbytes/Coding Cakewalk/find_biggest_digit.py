"""
    Given a number x, you have to calculate the biggest digit present in the string.
"""


# Solution 1
# number = list(map(int, input()))
# print(max(number))



# Solution 2
number = int(input())

max_digit = 0

while number != 0:

    temp = number % 10
    if temp > max_digit:
        max_digit = temp
    number = number // 10

print(max_digit)