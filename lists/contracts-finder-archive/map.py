#!/usr/bin/env python3

import sys
import csv


for line in sys.stdin:
    if line.strip() == '':
        break

#PublicSectorBodyName,CFBuyerGroupID,ParentCFBuyerGroupID

print("name")

for row in csv.DictReader(sys.stdin):
    name = row['PublicSectorBodyName'].strip()
    name = name.replace("&#39;", "'")
    print(name)
