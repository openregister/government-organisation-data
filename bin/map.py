#!/usr/bin/env python3

import re
import sys
import csv

# usage
key = sys.argv[1]
code = sys.argv[2]
fixup_path = sys.argv[3]
name_path = sys.argv[4]

names = {}
codes = {}

sep = '\t'
fields = [code, key]

# normalise name
def n7e(s):
    return ' '.join(s.split()).strip().lower()

# read name map
for row in csv.DictReader(open(name_path), delimiter=sep):
    names[n7e(row['name'])] = row[key]

# read source list
for row in csv.DictReader(sys.stdin, delimiter=sep):
    name = n7e(row['name'])
    if name in names:
        codes[row[code]] = names[name]

    if key in row:
        codes[row[code]] = row[key]

# assert fixup codes
for row in csv.DictReader(open(fixup_path), delimiter=sep):
    codes[row[code]] = row[key]


# print map
print(sep.join(fields))

for c in sorted(codes):
    row = { code: c, key: codes[c] }
    print(sep.join([row[field] for field in fields]))
