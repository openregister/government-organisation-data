#
#  target register data
#
REGISTER=data/government-organisation/government-organisation.tsv

#
#  report of lists, maps and the register
#
REPORT=report/index.html

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
	maps/abbreviation.tsv\
	maps/name.tsv\
	maps/govuk.tsv

all: $(REGISTER) $(MAPS) $(REPORT)

$(REGISTER):	bin/government-organisation.py $(FIXUPS) $(SOURCE)
	@mkdir -p data/government-organisation
	python3 bin/government-organisation.py $(FIXUPS) < $(SOURCE) > $@

maps/govuk.tsv:	$(SOURCE) $(REGISTER) bin/govuk.py
	@mkdir -p maps
	python3 bin/govuk.py $(REGISTER) < $(SOURCE) > $@

maps/name.tsv:	$(REGISTER) fixup/word.tsv maps/abbreviation.tsv fixup/name.tsv $(LISTS) bin/name.py
	@mkdir -p maps
	python3 bin/name.py fixup/word.tsv maps/abbreviation.tsv fixup/name.tsv $(LISTS) < $(REGISTER) > $@

maps/abbreviation.tsv:	$(SOURCE) fixup/abbreviation.tsv bin/abbreviation.py
	@mkdir -p maps
	python3 bin/abbreviation.py fixup/abbreviation.tsv < $(SOURCE) > $@

$(REPORT):	$(REGISTER) $(LISTS) $(MAPS) maps/index.yml lists/index.yml bin/report.py
	@mkdir -p report
	python3 bin/report.py report/lists/ > $@

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
