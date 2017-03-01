#!/usr/bin/env python3

import sys
import openpyxl

fields = ['miso', 'name', 'type']
sep = '\t'

wb = openpyxl.load_workbook(sys.argv[1])
sh = wb.get_active_sheet()

print(sep.join(fields))

for r in sh.rows:

    row = {}
    row['miso'] = r[0].value
    row['name'] = r[1].value
    row['sector'] = r[8].value
    row['type'] = r[9].value

    if row['miso'] == 'URN':
        continue

    print(sep.join([str(row[field]) for field in fields]))
