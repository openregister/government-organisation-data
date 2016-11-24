#!/usr/bin/env python3

import sys

code = []
left = True

for line in sys.stdin:
    if line[0] == chr(12):
        line = line[1:]
        left = True

    line = line.strip()

    if line == 'Code':
        line = "coins"
    elif line == 'Description':
        line = "name"

    if line == '':
        left = False
        continue

    if left:
        code.append(line)
    else:
        print("%s\t%s" % (code.pop(0), line))
