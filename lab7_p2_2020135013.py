"""
CCO1100-01 Lab 7
Programming Problems
Problem 2
"""

# read txt
text = open("./input_7_2.txt", 'r')
string = text.read()

# make dictionary
dic = {}
for i in string:
    if i.isalpha():
        i = i.upper()
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

# sorted list
sorting = []
num = 1
length = 0
while length < len(dic):
    if num in dic.values():
        keys = []
        for i in range(len(dic)):
            key, value = list(dic.items())[i]
            if value == num:
                keys.append(key)
                length += 1
    
        keys.sort()
        sorting.append(keys)
    num += 1

# print result
sorting = sorting[::-1]
result = []
for i in range(len(sorting)):
    result += sorting[i]

print(result)