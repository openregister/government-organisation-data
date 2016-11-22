NAME=$(shell basename ${PWD})

# see: http://www.legislation.gov.uk/uksi/2015/1655/made
URL=http://legislation.data.gov.uk/uksi/2015/1655/made/data.xml

XML=$(NAME).xml
TSV=$(NAME).tsv
CMD=$(NAME).sh
XSL=$(NAME).xsl

$(TSV):	$(XML) $(CMD) $(XSL)
	$(CMD) < $(XML) > $@

$(XML):
	curl -s $(URL) > $@

clean:
	rm -f $(XML) $(TSV)
