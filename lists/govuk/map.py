#!/usr/bin/env python3

import json
import sys

fields = ['government-organisation', 'name', 'website']

field_map = {
    'name': 'title',
    'government-organisation': 'analytics_identifier',
    'website': 'web_url'
}

sep = '\t'

print(sep.join(fields))

for line in sys.stdin:
    r = json.loads(line)

    row = {}
    print(sep.join([r[field_map[field]] for field in fields]))
