#!/usr/bin/env python3

import sys
import csv

# "Holding ID","Property Number","Holding Number","Department Property Ref","Department Holding Ref","Department","Organisation","Longitude","Latitude","Area (ha)","Holding Name","Property Name","Street No","Road","District","PostTown","County","PostCode","Local Authority","Usage","Holding Type"

orgs = {}

def add(s):
    s = s.strip()
    if s == '':
        return
    orgs[s] = 1

for row in csv.DictReader(sys.stdin):
    add(row['Department'])
    add(row['Organisation'])

print("name")
for org in sorted(orgs):
    print(org)
