DATA=\
	data/government-organisation/government-organisation.tsv

MAPS=

all: $(DATA) $(MAPS)

data/government-organisation/government-organisation.tsv: fixup/government-organisation.tsv lists/govuk/list.tsv bin/government-organisation.py
	@mkdir -p data/government-organisation
	python3 bin/government-organisation.py fixup/government-organisation.tsv < lists/govuk/list.tsv > $@


#
#  python ..
#
init::
	pip3 install -r requirements.txt

flake8:
	flake8 bin

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
