# see: http://www.legislation.gov.uk/uksi/2012/1803/contents/made
URL=http://legislation.data.gov.uk/uksi/2012/1803/made/data.xml

tooldir=.

list.tsv:	data.xml $(tooldir)/map.sh $(tooldir)/map.xsl
	$(tooldir)/map.sh < data.xml > $@

data.xml:
	curl -s $(URL) > $@

clean:
	rm -f data.xml list.tsv
