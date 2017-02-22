#!/usr/bin/env python3

# download paginated json as jsonl

import sys
import requests
import json

page = 1
pages = 2
while page < pages:
    url = "https://www.gov.uk/api/organisations?page=%d" % (page)
    resp = requests.get(url=url)
    r = json.loads(resp.text)
    pages = r['pages']
    page = page + 1

    for row in r['results']:
        json.dump(row, sys.stdout)
        print()
