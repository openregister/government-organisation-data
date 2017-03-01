#!/usr/bin/env python3

import sys
from xlrd import open_workbook

book = open_workbook(sys.argv[1])
sheet = book.sheet_by_name('Index')

print('name')

for row in range(sheet.nrows):
    s = sheet.cell(row, 0).value
    if s == '' or s == 'Index' or s == 'Institutions':
        continue
    print(s)
