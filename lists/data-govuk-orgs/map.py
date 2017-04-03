#!/usr/bin/env python3

import json
import sys

fields = ['data-govuk-org', 'name', 'slug']

field_map = {
    'data-govuk-org': 'id',
    'name': 'title',
    'slug': 'name'
}

sep = '\t'

print(sep.join(fields))

for line in sys.stdin:
    r = json.loads(line)

    row = {}
    print(sep.join([r[field_map[field]].strip() for field in fields]))
