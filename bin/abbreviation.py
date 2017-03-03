#!/usr/bin/env python3

import re
import sys
import csv

fields = ['abbreviation', 'government-organisation']
sep = '\t'

abbreviations = {}
abbreviation_path = sys.argv[1]

def n7e(s):
    return s.lower().strip()

# read source data
for row in csv.DictReader(sys.stdin, delimiter=sep):
    if 'abbreviation' in row and row['abbreviation']:
        abbreviations[n7e(row['abbreviation'])] = row

# assert fixups
for row in csv.DictReader(open(abbreviation_path), delimiter=sep):
    abbreviations[n7e(row['abbreviation'])] = row

print(sep.join(fields))

for abbreviation in sorted(abbreviations):
    row = abbreviations[abbreviation]

    row['abbreviation'] = n7e(row['abbreviation'])

    if (row['government-organisation']):
        print(sep.join([row[field] for field in fields]))
