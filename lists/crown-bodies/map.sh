#!/bin/sh

echo name
grep "^<li>" |
  grep -v 'name=' |
  sed \
  -e 's/^<li> *//' \
  -e "s/\&#8217;/'/g" \
  -e 's/\&amp;/\&/g' \
  -e 's/<\/li>.*$//'
