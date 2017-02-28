#!/usr/bin/env python3

import sys
import csv

fields = ['government-organisation', 'name', 'website', 'start-date', 'end-date']
sep = '\t'

# fixup by website
website = {}
for row in csv.DictReader(open(sys.argv[1]), delimiter=sep):
    website[row['website']] = row


def defval(row, field):
    if field in row and row[field]:
        return row[field]

    if row['website'] in website:
        return website[row['website']].get(field, '')

    return ''

print(sep.join(fields))

for row in csv.DictReader(sys.stdin, delimiter=sep):

    row['start-date'] = defval(row, 'start-date')
    row['end-date'] = defval(row, 'end-date')

    if row['end-date'] == 'closed':
        row['end-date'] = ''

    print(sep.join([row[field] for field in fields]))
