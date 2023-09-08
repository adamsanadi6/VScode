"""

Given an array of integers, you have to find if any number in the array is divisible by 5 or Not

"""

numbers = list(map(int, input().split()))

for number in numbers:
    if number % 5 == 0:
        print("Yes")
        break
else:
    print("No")