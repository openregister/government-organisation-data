# see: https://data.gov.uk/data/dumps
URL=https://data.gov.uk/data/dumps/data.gov.uk-ckan-meta-data-latest.organizations.jsonl.gz

list.tsv:	resources.jsonl map.py
	python3 map.py < resources.jsonl > $@

resources.jsonl:
	curl -s $(URL) | gzip -d -c > resources.jsonl

clean:
	rm -f resources.jsonl list.tsv
