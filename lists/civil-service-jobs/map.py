#!/usr/bin/env python3

import sys
from html.parser import HTMLParser

orgs = {}

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'select':
            self.add = ('id', 'nghr_dept') in attrs

    def handle_data(self, data):
        data = data.strip()
        if data and getattr(self, 'add', False):
            print(data)

    def handle_endtag(self, tag):
        if tag == 'select':
            self.add = False

print("name")

parser = MyHTMLParser()
parser.feed(sys.stdin.read())
