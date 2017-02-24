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

def array_to_string(arr, pre_process):
    res = ""
    first = True
    for i in arr:
        if first:
            first = False
        else:
            res += ";"
        res += pre_process(i)
    return res


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

print(sep.join(fields))

for line in sys.stdin:
    r = json.loads(line)

    r['parent-govuks'] = array_to_string(r['parent_organisations'], lambda x: x['id'].rsplit('/', 1)[1])

    print(sep.join([json_path(r, field_path[field]) for field in fields]))
