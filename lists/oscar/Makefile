# see: https://www.gov.uk/government/publications/oscar-publishing-data-from-the-database-september-2016
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/554102/OSCAR_in-year_dataset_21Sep2016.xlsx

list.tsv:	data.xlsx map.py
	python3 map.py data.xlsx > $@

data.xlsx:
	curl -s $(URL) > $@

clean:
	rm -f data.xlsx list.tsv

init:
	pip install -r requirements.txt
