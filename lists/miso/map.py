#!/usr/bin/env python3

import sys
import openpyxl

fields = ['urn', 'name', 'type']
sep = '\t'

wb = openpyxl.load_workbook(sys.argv[1])
sh = wb.get_active_sheet()

print(sep.join(fields))

for r in sh.rows:

    row = {}
    row['urn'] = r[0].value
    row['name'] = r[1].value
    row['sector'] = r[8].value
    row['type'] = r[9].value

    if row['urn'] == 'URN':
        continue

    if row['sector'] != 'Central Government':
        continue

    if row['type'] in ['RAF', 'Army', 'Navy']:
        continue

    print(sep.join([str(row[field]) for field in fields]))
