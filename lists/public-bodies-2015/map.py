#!/usr/bin/env python3

import io
import sys
import csv

"""
Number of Bodies,Name,Department,Classification,PB Reform,Regulatory Function,Description/Terms of Reference,Notes,Address,Phone,Email,Website,Chair,Chair's Remuneration (p.a. unless otherwise stated),Chief Executive / Secretary,Chief Executive / Secretary Remuneration,Public Meetings,Public Minutes,Register of Interests,Ombudsman,Last Annual Report,Last Review,Government Funding,Total Gross Expenditure,Staff employed,Audit Arrangements,OCPA Regulated,Chair Ministerial or non-ministerial Appt,"ChairPaid or unpaid","ChairNo.Male","ChairNo.Female","ChairNo.Gender Unknown/ undeclared","MembersMinisterial or non-ministerial Appt","MembersPaid or unpaid?","MembersNo. Male","MembersNo. Female","MembersNo. Gender Unknown/ undeclared",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""

blacklist = [
    "arm's length bodies abolished before 31st March 2015 show zero in Number of Bodies column",
    "Cabinet Office and DCMS (joint accountability)"
]

orgs = {}

def add(s):
    s = s.replace('Õ', "'")
    s = s.replace('Ê', "-")
    s = s.replace('(x47)', "")
    s = s.replace('(x9)', "")
    s = s.replace('(x 13)', "")
    s = s.replace("Treasury Solicitor's Department (known as Government Legal Department from 1.4.15)", "Government Legal Department")
    s = s.strip()
    if s == '':
        return
    if s not in blacklist:
        orgs[s] = 1

stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

for row in csv.DictReader(stream):
    add(row['Department'])
    add(row['Name'])

print("name")
for org in sorted(orgs):
    print(org)
