#!/usr/bin/env python3

import sys
from xlrd import open_workbook

book = open_workbook(sys.argv[1])
sheet = book.sheet_by_name('PB 2012')

names = {}

for row in range(sheet.nrows):
    name = sheet.cell(row, 1).value
    if name != 'name':
        names[name] = 1

    department = sheet.cell(row, 2).value
    if department != 'department':
        names[department] = 1

print('name')
for name in sorted(names):
    print(name)
