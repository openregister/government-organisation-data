
#!/usr/bin/env python3

import sys
import csv

fields = ['govuk', 'government-organisation']
sep = '\t'

print(sep.join(fields))

for row in csv.DictReader(sys.stdin, delimiter=sep):
    print(sep.join([row[field] for field in fields]))
