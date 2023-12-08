"""
CCO1100-01 Lab 7
Programming Problems
Problem 1
"""

# import regular expression module
import re

# read txt
text = open("./input_7_1.txt", 'r')
string = text.read()
string = string.split("\n")

# delete annotation
an2_1, an2_2 = -1, -1
for i in range(len(string)):
    # find an1 (#)
    if '#' in string[i]:
        an1 = string[i].index('#')
        string[i] = string[i][:an1]
    
    # find another an2
    if an2_1 != -1 and '"""' in string[i]:
        for j in range(an2_1, i+1):
            string[j] = ''
        an2_1 = -1
    if an2_2 != -1 and "'''" in string[i]:
        for j in range(an2_2, i+1):
            string[j] = ''
        an2_2 = -1
        
    # find an2 (""" or ''')
    if '"""' in string[i]:
        an2_1 = i
    if "'''" in string[i]:
        an2_2 = i

# (do not) delete empty line
lines = string

# find def
defs, defs_line = [], []
re_defs = re.compile('^def .*')
for i in range(len(lines)):
    if len(re_defs.findall(lines[i])) > 0:
        last = lines[i].index("(")
        defs.append(re_defs.findall(lines[i])[0][4:last])
        defs_line.append(i+1)

# compile re
test = re.compile('a\(.')
for i in range(len(defs)):
    re_call = re.compile(defs[i] + '\(.*\)')
    defs_call = []
    for j in range(defs_line[i], len(lines)):
        if len(re_call.findall(lines[j])) > 0:
            defs_call.append(j + 1)
    
    # print result
    print(f"{defs[i]}: def in " + str(defs_line[i]) + ", calls in", defs_call)
