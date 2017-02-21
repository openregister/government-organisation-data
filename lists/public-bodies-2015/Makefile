# see: https://www.gov.uk/government/publications/public-bodies-2015
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/506888/PB2015_Directory_Dataset_final_Jan_2016.csv

list.tsv:	data.csv map.py
	python3 map.py < data.csv > $@

data.csv:
	curl -s $(URL) | iconv -f ISO8859-1 -t UTF-8 > $@

clean:
	rm -f data.csv list.tsv
