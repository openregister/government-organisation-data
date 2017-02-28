#!/usr/bin/env python3

import json
import sys

fields = ['government-organisation', 'abbreviation', 'government-organisation-type', 'govuk', 'name', 'website', 'parent-govuks']

field_path = {
    'government-organisation': 'analytics_identifier',
    'government-organisation-type': 'format',
    'govuk': 'details/slug',
    'name': 'title',
    'website': 'web_url',
    'parent-govuks': 'parent-govuks',
    'abbreviation': 'details/abbreviation'
}


def json_path(d, path):
    e = d
    try:
        for p in path.split("/"):
            e = e.get(p)
    except:
        pass

    if not e:
        e = ''

    return e


sep = '\t'
list_sep = ';'

print(sep.join(fields))

for line in sys.stdin:
    r = json.loads(line)

    r['parent-govuks'] = list_sep.join(o['id'].rsplit('/', 1)[1] for o in r['parent_organisations'])

    print(sep.join([json_path(r, field_path[field]).replace(sep, '') for field in fields]))
