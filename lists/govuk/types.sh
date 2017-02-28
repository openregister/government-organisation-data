#!/bin/sh

echo "government-organisation-type\tcount"

tail -n +2 |
  cut -d'	' -f3 |
  sort |
  uniq -c |
  sed -e 's/^ *//' -e 's/ /	/' |
  awk -F'	' '{ print $2 "	" $1 }'
