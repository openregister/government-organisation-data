#!/usr/bin/env python3

import re
import sys
import csv

# usage
word_path = sys.argv[1]
abbreviation_path = sys.argv[2]
name_path = sys.argv[3]
paths = sys.argv[4:]

names = {}
register = {}
abbreviations = {}
words = {}
codes = {}

fields = ['name', 'government-organisation']
sep = '\t'

def _n7e(s):
    return ' '.join(s.split()).strip().lower()

def n7e(s):
    c = s
    s = _n7e(s)

    # remove "(x99)" and the like
    s = re.sub('(x[0-9]*)', '', s)

    # remove non-latin-alphanumerics
    s = re.sub('[^a-z0-9 ]', '', s)

    # Her Majesty's -> HM
    s = re.sub('her majestys', 'hm', s)

    # translate words
    w = [words.get(word, word) for word in s.split()]

    # remove a leading or trailing known abbreviation
    # - may introduce false positives
    if len(w) > 1:
        if w[-1] in abbreviations:
            w = w[:-1]

    if len(w) > 1:
        if w[0] in abbreviations:
            w = w[1:]

    # remove trailing "Department of" / "Department for"

    if len(w) > 2 and w[-2] == 'department' and w[-1] in ['for', 'of']:
        w = w[-2:] + w[:-2]

    # join words and normalize spaces (again)
    s = ' '.join(w)
    return _n7e(s)


def add(name, code=''):
    n = n7e(name)

    if n not in names:
        names[n] = { 'names': {}, 'government-organisation': {} }

    if code:
        names[n]['government-organisation'][code] = 1

    names[n]['names'][name] = 1


# read normalised words
for row in csv.DictReader(open(word_path), delimiter=sep):
    words[_n7e(row['word'])] = row['normalised']

# read abbreviations
for row in csv.DictReader(open(abbreviation_path), delimiter=sep):
    abbreviations[_n7e(row['abbreviation'])] = row.get('government-organisation', '')

# read register data
for row in csv.DictReader(sys.stdin, delimiter=sep):
    register[row['government-organisation']] = row
    add(row['name'], row['government-organisation'])

# read lists for names
for path in paths:
    for row in csv.DictReader(open(path), delimiter=sep):
        name = row['name'].strip()
        code = abbreviations.get(n7e(name), row.get('government-organisation', ''))
        add(name, code)

# assert fixup codes
for row in csv.DictReader(open(name_path), delimiter=sep):
    names[n7e(row['name'])]['government-organisation'][row['government-organisation']] = 1

print(sep.join(fields))
for n in sorted(names):
    for name in sorted(names[n]['names']):
        row = {}
        row['name'] = name

        orgs = [org for org in names[n]['government-organisation'] if org in register]

        row['government-organisation'] = ';'.join(sorted(orgs))

        print(sep.join([row[field] for field in fields]))
