
#!/usr/bin/env python3

import sys
import csv

fields = ['govuk', 'government-organisation']
sep = '\t'

print(sep.join(fields))

# read register data
government_organisation = {}
for row in csv.DictReader(open(sys.argv[1]), delimiter=sep):
    government_organisation[row['government-organisation']] = row

for row in csv.DictReader(sys.stdin, delimiter=sep):

    if row['government-organisation'] not in government_organisation:
        row['organisations'] = ''

    print(sep.join([row[field] for field in fields]))
