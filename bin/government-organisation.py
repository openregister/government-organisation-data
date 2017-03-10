#!/usr/bin/env python3

import sys
import csv

fields = ['government-organisation', 'name', 'website', 'start-date', 'end-date']
sep = '\t'

# fixup by website
website = {}
for row in csv.DictReader(open(sys.argv[1]), delimiter=sep):
    website[row['website']] = row

# entries to exclude from the register
blacklist = {}
for row in csv.DictReader(open(sys.argv[2]), delimiter=sep):
    blacklist[row['government-organisation']] = row


def default(row, field):
    if field in row and row[field]:
        return row[field]

    if row['website'] in website:
        return website[row['website']].get(field, '')

    return ''

def usurp(row, field):
    if row['website'] in website and website[row['website']][field]:
        return website[row['website']][field]

    return row[field]

print(sep.join(fields))

for row in csv.DictReader(sys.stdin, delimiter=sep):

    if row['government-organisation'] not in blacklist:
        row['name'] = usurp(row, 'name').strip()
        row['start-date'] = default(row, 'start-date')
        row['end-date'] = default(row, 'end-date')

        if row['end-date'] == 'closed':
            row['end-date'] = ''

        print(sep.join([row[field] for field in fields]))
