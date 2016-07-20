# Government organisation register data

Data for the prototype [government-organisation register](http://government-organisation.openregister.org),
a list of UK central government organisations seeded from [GOV.UK](https://www.gov.uk/government/organisations).

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
