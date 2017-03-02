# see: https://www.gov.uk/government/publications/public-bodies-reports
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/223945/Public_Bodies_2012_1.xls

list.tsv:	data.xls map.py
	python3 map.py data.xls > $@

data.xls:
	curl -s $(URL) > $@

clean:
	rm -f data.xls list.tsv

init:
	pip install -r requirements.txt
