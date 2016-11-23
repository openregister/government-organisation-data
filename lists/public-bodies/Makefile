# see: https://www.gov.uk/government/publications/public-bodies-2013
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/329438/PBQ_update_as_at_31-03-2014.xls

list.tsv:	data.xls map.py
	map.py data.xls > $@

data.xls:
	curl -s $(URL) > $@

clean:
	rm -f data.csv list.tsv

init:
	pip install -r requirements.txt
