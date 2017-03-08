# Government organisation register data

Data for an alpha register of UK central government organisations — departments, agencies and other organisations with a presence on GOV.UK:

  * [data/government-organisation/government-organisation.tsv](data/government-organisation/government-organisation.tsv)

The term "public sector" or "public body" has a much wider scope than central government organisations covered by this register.
The meaning of "public sector" depends upon context, for example, the Digital Marketplace buyers list includes schools, academies, public corporations and other legal entities such as charities funded by government and recorded in separate registers.

A register needing to reference public sector organisations may use a "public-body", "organisation", "operator" or other field which is a CURIE to one of a number of different registers, including the government-organisation register.

# Lists, fixes and maps

See https://openregister.github.io/report

# Other lists

There are older PDF reports on [public bodies 1999-2009](https://www.gov.uk/government/publications/public-bodies-reports-1999-to-2009) and in the [GOV.UK public bodies collection](https://www.gov.uk/government/collections/public-bodies).

This list of lists is by no means comprehensive, and contributions of other lists are appreciated.


# Building

Use make to build register shaped data
– we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 government-organisation-data
    $ workon government-organisation-data
    $ make init

    $ make

# Licence

The software in this project is covered by LICENSE file.

The data is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
