# see: https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/datasets/publicsectorclassificationguide
URL=https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/uksectoraccounts/datasets/publicsectorclassificationguide/october2016/publicsectorclassificationguidelatest.xls

list.tsv:	data.xls map.py
	python3 map.py data.xls > $@

data.xls:
	curl -s $(URL) > $@

clean:
	rm -f data.xls list.tsv

init:
	pip install -r requirements.txt
