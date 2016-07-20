data/government-organisation: bin/map.py
	mkdir -p data/government-organisation
	bin/map.py > data/government-organisation/government-organisations.tsv

#
#  code
#
init::
	pip3 install -r requirements.txt

flake8:
	flake8 bin

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
