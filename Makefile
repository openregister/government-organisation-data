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

CLOUDSTORE_BUYER_LIST=lists/cloudstore-buyers/list.tsv
COINS_LIST=lists/coins/list.tsv
CONTRACTS_FINDER_LIST=lists/contracts-finder/list.tsv
DATA_GOVUK_ORG_LIST=lists/data-govuk-orgs/list.tsv
MISO_LIST=lists/miso/list.tsv
OSCAR_LIST=lists/oscar/list.tsv

LISTS=$(wildcard lists/*/list.tsv)

#
#  source fixup data used to translate a list into register
#
FIXUPS=\
	fixup/government-organisation.tsv\
	fixup/blacklist.tsv\
	\
	fixup/abbreviation.tsv\
	fixup/name.tsv\
	fixup/word.tsv

#
#  maps generated to find register records from values found in lists
#
MAPS=\
	maps/abbreviation.tsv\
	maps/govuk.tsv\
	maps/name.tsv\
	maps/coins.tsv\
	maps/cloudstore-buyer.tsv\
	maps/data-govuk-org.tsv\
	maps/buyer-id.tsv\
	maps/miso.tsv\
	maps/oscar.tsv

all: $(REGISTER) $(MAPS) $(REPORT)

$(REGISTER):	bin/government-organisation.py $(FIXUPS) $(SOURCE)
	@mkdir -p data/government-organisation
	python3 bin/government-organisation.py $(FIXUPS) < $(SOURCE) > $@

#
# maps
#
maps/govuk.tsv:	$(SOURCE) $(REGISTER) bin/govuk.py
	@mkdir -p maps
	python3 bin/govuk.py $(REGISTER) < $(SOURCE) > $@

maps/name.tsv:	$(REGISTER) fixup/word.tsv maps/abbreviation.tsv fixup/name.tsv $(LISTS) bin/name.py
	@mkdir -p maps
	python3 bin/name.py fixup/word.tsv maps/abbreviation.tsv fixup/name.tsv $(LISTS) < $(REGISTER) > $@

maps/abbreviation.tsv:	$(REGISTER) $(SOURCE) fixup/abbreviation.tsv bin/abbreviation.py
	@mkdir -p maps
	python3 bin/abbreviation.py $(REGISTER) fixup/abbreviation.tsv < $(SOURCE) > $@

maps/oscar.tsv:	$(REGISTER) $(OSCAR_LIST) fixup/oscar.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation oscar fixup/oscar.tsv maps/name.tsv < $(OSCAR_LIST) > $@

maps/coins.tsv:	$(REGISTER) $(COINS_LIST) fixup/coins.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation coins fixup/coins.tsv maps/name.tsv < $(COINS_LIST) > $@

maps/cloudstore-buyer.tsv:	$(REGISTER) $(CLOUDSTORE_BUYER_LIST) fixup/cloudstore-buyer.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation cloudstore-buyer fixup/cloudstore-buyer.tsv maps/name.tsv < $(CLOUDSTORE_BUYER_LIST) > $@

maps/buyer-id.tsv:	$(REGISTER) $(CONTRACTS_FINDER_LIST) fixup/buyer-id.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation buyer-id fixup/buyer-id.tsv maps/name.tsv < $(CONTRACTS_FINDER_LIST) > $@

maps/data-govuk-org.tsv:	$(REGISTER) $(DATA_GOVUK_ORG_LIST) fixup/data-govuk-org.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation data-govuk-org fixup/data-govuk-org.tsv maps/name.tsv < $(DATA_GOVUK_ORG_LIST) > $@

maps/miso.tsv:	$(REGISTER) $(MISO_LIST) fixup/miso.tsv maps/name.tsv bin/map.py
	@mkdir -p maps
	python3 bin/map.py government-organisation miso fixup/miso.tsv maps/name.tsv < $(MISO_LIST) > $@

#
# report
#
$(REPORT):	$(REGISTER) $(LISTS) $(MAPS) maps/index.yml lists/index.yml bin/report.py
	@mkdir -p report
	python3 bin/report.py report/lists/ > $@


# remove targets
clobber:
	rm -f $(REGISTER) $(DATA) $(MAPS)

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
