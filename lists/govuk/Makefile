# download raw list from https://www.gov.uk/api/organisations?page=1

all:	list.tsv types.tsv

list.tsv:	data.jsonl map.py
	python3 map.py < data.jsonl > $@

data.jsonl:	download.py
	python3 download.py > $@

types.tsv:	list.tsv types.sh
	./types.sh < list.tsv > $@

init:
	pip install -r requirements.txt
