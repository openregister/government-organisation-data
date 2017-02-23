# see: https://www.civilservicejobs.service.gov.uk/csr/index.cgi
URL='https://www.civilservicejobs.service.gov.uk/csr/index.cgi'

list.tsv:	data.html map.py
	python3 map.py < data.html > $@

data.html:
	curl -s $(URL) | iconv -f ISO8859-1 -t UTF-8 > $@

clean:
	rm -f data.html list.tsv
