#!/usr/bin/env python3

import re
import sys
import csv

fields = ['name', 'government-organisation']
sep = '\t'

names = {}

def n7e(s):
    s = s.lower()
    s = re.sub('[^a-z0-9 ]', '', s)
    s = re.sub('(x[0-9]*)', '', s)
    s = re.sub('committees', 'committee', s)
    ignore = ['and', 'the', 'ago', 'bis', 'beis', 'defra', 'fera', 'fsa']
    words = [word for word in s.split() if word not in ignore]
    s = ' '.join(words)
    s = s.strip()
    return s

def add(name, code=''):
    n = n7e(name)
    if n not in names:
        names[n] = { 'names': {}, 'government-organisation': '' }

    if code:
        names[n]['government-organisation'] = code

    names[n]['names'][name] = 1

# read register data
government_organisation = {}
for row in csv.DictReader(sys.stdin, delimiter=sep):
    add(row['name'], row['government-organisation'])

# read lists for names
for list in sys.argv[1:]:
    for row in csv.DictReader(open(list), delimiter=sep):
        add(row['name'], row.get('government-organisation', ''))

print(sep.join(fields))

for n in sorted(names):
    for name in sorted(names[n]['names']):
        row = {}
        row['name'] = name
        row['government-organisation'] = names[n]['government-organisation']
        print(sep.join([row[field] for field in fields]))
