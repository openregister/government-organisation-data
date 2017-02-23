#!/usr/bin/env python3

# download paginated json as jsonl

import sys
import requests
import json

url = "https://www.gov.uk/api/organisations?page=1"

while url:
    resp = requests.get(url=url)
    r = json.loads(resp.text)

    for row in r['results']:
        json.dump(row, sys.stdout)
        print()

    if 'next_page_url' in r:
        url = r['next_page_url']
    else:
        url = None
