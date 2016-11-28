# see: https://www.epims.ogc.gov.uk/government-property-finder/Home.aspx

# no cool URLs, so built from a saved copy:
CSV=cache/PropertyHoldingExport_25-11-2016.csv

list.tsv:	$(CSV) map.py
	map.py < $(CSV) > $@

clean:
	rm -f list.tsv
