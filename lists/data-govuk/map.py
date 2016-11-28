#!/usr/bin/env python3

import sys
import csv

# Dataset Name,URL,Format,Description,Resource ID,Position,Date,Organization,Top level organization

orgs = {}

for row in csv.DictReader(sys.stdin):
    orgs[row['Organization']] = 1
    orgs[row['Top level organization']] = 1

print("name")
for org in sorted(orgs):
    print(org)
