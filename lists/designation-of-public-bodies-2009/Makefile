# see: http://www.legislation.gov.uk/uksi/2009/1973/contents/made
URL=http://legislation.data.gov.uk/uksi/2009/1973/made/data.xml
tooldir=../designation-of-public-bodies-2015

list.tsv:	data.xml $(tooldir)/map.sh $(tooldir)/map.xsl
	$(tooldir)/map.sh < data.xml > $@

data.xml:
	curl -s $(URL) > $@

clean:
	rm -f data.xml list.tsv
