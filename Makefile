#
#  target register data
#
REGISTER=data/government-organisation/government-organisation.tsv

#
#  source GOV.UK list
#
SOURCE=lists/govuk/list.tsv

LISTS=$(wildcard lists/*/list.tsv)

#
#  source fixup data used to translate a list into register
#
FIXUPS=\
	fixup/government-organisation.tsv

#
#  maps generated to find register records from values found in lists
#
MAPS=\
	maps/name.tsv\
	maps/govuk.tsv

all: $(REGISTER) $(MAPS)

$(REGISTER):	bin/government-organisation.py $(FIXUPS) $(SOURCE)
	@mkdir -p data/government-organisation
	python3 bin/government-organisation.py $(FIXUPS) < $(SOURCE) > $@

maps/govuk.tsv:	$(SOURCE) $(REGISTER) bin/govuk.py
	@mkdir -p maps
	python3 bin/govuk.py $(REGISTER) < $(SOURCE) > $@

maps/name.tsv:	$(REGISTER) $(LISTS) bin/name.py
	@mkdir -p maps
	python3 bin/name.py $(LISTS) < $(REGISTER) > $@

# remove targets
clobber:
	rm -f $(DATA) $(MAPS)

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
