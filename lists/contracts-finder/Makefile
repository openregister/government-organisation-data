URL='https://www.contractsfinder.service.gov.uk/Notice/Summary'

list.tsv:	data.html map.sh
	./map.sh < data.html > $@

data.html:
	curl -s $(URL) > $@

clean:
	rm -f data.html list.tsv
