# see: http://www.legislation.gov.uk/uksi/2015/1655/made
URL=http://legislation.data.gov.uk/uksi/2015/1655/made/data.xml

list.tsv:	data.xml map.sh map.xsl
	map.sh < data.xml > $@

data.xml:
	curl -s $(URL) > $@

clean:
	rm -f data.xml list.tsv
