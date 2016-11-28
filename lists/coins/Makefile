# see: https://www.whatdotheyknow.com/cy/request/list_of_public_bodies_in_the_coi#incoming-69457
URL='https://www.whatdotheyknow.com/cy/request/26677/response/69457/attach/3/Oranisation%20list%20ex%20COINS%2022%20Jan%2010.pdf'

# uses https://en.wikipedia.org/wiki/Pdftotext which is bundled with poppler https://en.wikipedia.org/wiki/Poppler_(software)

list.tsv:	data.txt map.py
	map.py < data.txt > $@

data.txt:	data.pdf
	pdftotext data.pdf $@

data.pdf:
	curl -s $(URL) > $@

clean:
	rm -f data.pdf data.txt list.tsv
