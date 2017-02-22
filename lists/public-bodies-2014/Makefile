# see: https://www.gov.uk/government/publications/public-bodies-2014
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/371670/Annex_A_i_public_bodies_2014_for_publication.csv

list.tsv:	data.csv map.py
	python3 map.py < data.csv > $@

data.csv:
	curl -s $(URL) | iconv -f ISO8859-1 -t UTF-8 > $@

clean:
	rm -f data.csv list.tsv
