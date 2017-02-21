#!/usr/bin/env python3

import sys
from xlrd import open_workbook

book = open_workbook(sys.argv[1])
sheet = book.sheet_by_name('Full data')

for row in range(sheet.nrows):
    print(sheet.cell(row, 1).value)
