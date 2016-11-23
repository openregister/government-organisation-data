# Government organisation register data

Discovery data for the [government-organisation register](http://government-organisation.openregister.org),
a list of UK central government organisations seeded from [GOV.UK](https://www.gov.uk/government/organisations).

# Lists

The data is being compiled from existing lists of organisations found in government data:

- [govuk](lists/govuk/list.tsv) — [GOV.UK government organisations](https://www.gov.uk/government/organisations)
- [whole-of-government-accounts](lists/whole-of-government-accounts/list.tsv) — [The Whole of Government Accounts (Designation of Bodies) Order 2015](http://www.legislation.gov.uk/uksi/2015/1655/made)
- [data-govuk](lists/data-govuk/list.tsv) — [data.gov.uk publishers](https://data.gov.uk/publisher)
- [quangos](lists/quangos/list.tsv) — [Cabinet Office list of quangos (2013)](https://www.gov.uk/government/publications/public-bodies-2013)

This list is by no means comprehensive, and contributions of other lists are appreciated!

# Building

Use make to build register shaped data
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 government-organisation-data
    $ workon government-organisation-data
    $ make init

    $ make

# Licence

The software in this project is covered by LICENSE file.

The data is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
