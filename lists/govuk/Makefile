# download raw list from https://www.gov.uk/api/organisations?page=1

list.tsv:	data.jsonl map.py
	python3 map.py < data.jsonl > $@

data.jsonl:	download.py
	python3 download.py > $@

init:
	pip install -r requirements.txt
