"""
    One sentense is given, you have to find the which one is longest string. If there are two or more strings are having same length which is longest string then display the first string.
"""

string_list = list(input().split(' '))

max_len = 0
longest_string = None

for string in string_list:
    string_len = len(string)
    if string_len > max_len:
        max_len = string_len
        longest_string = string

print(longest_string)