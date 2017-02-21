# see: https://www.gov.uk/government/publications/public-bodies-2016
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/580163/public_bodies_data_set_for_gov_december_2016.csv

list.tsv:	data.csv map.py
	python3 map.py < data.csv > $@

data.csv:
	curl -s $(URL) | iconv -f ISO8859-1 -t UTF-8 > $@

clean:
	rm -f data.csv list.tsv
