# see: https://data.gov.uk/data/dumps
URL=https://data.gov.uk/data/dumps/data.gov.uk-ckan-meta-data-latest.csv.zip

list.tsv:	resources.csv map.py
	map.py < resources.csv > $@

resources.csv:
	curl -s $(URL) | bsdtar -xvf- resources.csv

clean:
	rm -f data.csv list.tsv
