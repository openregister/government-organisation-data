URL='http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/uk-crown-bodies/'

list.tsv:	data.html map.sh
	map.sh < data.html > $@

data.html:
	curl -s $(URL) > $@

clean:
	rm -f data.html list.tsv

