# Government organisation register data

Discovery data for a register of UK central government organisations.

# Lists

The data is being compiled from existing lists of organisations found in government data:

| List | Source |
| :---         |    :--- |
|[govuk](lists/govuk) |[GOV.UK government organisations](https://www.gov.uk/government/organisations)|
|[data-govuk](lists/data-govuk) |[data.gov.uk publishers](https://data.gov.uk/publisher)|
|[public-bodies](lists/public-bodies) |[Cabinet Office list of public bodies (2013)](https://www.gov.uk/government/publications/public-bodies-2013)|
|[designation-of-public-bodies](lists/designation-of-public-bodies) |[Whole of Government Accounts (Designation of Bodies) Order 2015](http://www.legislation.gov.uk/uksi/2015/1655/made)|
|[whole-of-government-accounts](lists/whole-of-government-accounts) |[Whole of Government Accounts (PDF report)](https://www.gov.uk/government/collections/whole-of-government-accounts)|
|[ons-public-sector-classification](lists/ons-public-sector-classification) |[ONS Public Sector Classification Guide](https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/datasets/publicsectorclassificationguide)|
|[crown-bodies](lists/crown-bodies) |[The National Archives list of crown bodies](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/uk-crown-bodies/)|
|[coins](lists/coins) |[Combined Online Information System (COINS) organisations](https://www.whatdotheyknow.com/cy/request/list_of_public_bodies_in_the_coi#incoming-69457)|


This list of lists is by no means comprehensive, and contributions of other lists are appreciated!

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
