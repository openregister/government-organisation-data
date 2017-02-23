# see: https://data.gov.uk/data/contracts-finder-archive/data-feeds/
URL='https://data.gov.uk/data/contracts-finder-archive/static/files/List_of_buying_organisations.csv'

list.tsv:	data.csv map.py
	python3 map.py < data.csv > $@

data.csv:
	curl -s $(URL) > $@

clean:
	rm -f data.csv list.tsv
