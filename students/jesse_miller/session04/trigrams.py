#!/usr/local/bin/python3
"""
Trigrams attempt
"""
with open("sherlock_small.txt", "r+") as f:
#    for str1 in file.readlines():
    lines = f.readlines()
sherlock = {}
current_key = None
for line in lines:
    line = line.strip()
    if not line:
        current_key = None
    elif not current_key:
        current_key = line
        sherlock[current_key] = []
    else:
        sherlock[current_key].append(line)
print(sherlock)
