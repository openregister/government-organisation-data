# Government organisation register data

Discovery data for a register of UK central government organisations — legal entities with a presence on GOV.UK.

Other organisations may be considered to be part of government for different processes, for example the Digital Marketplace
includes schools, academies, public corporations and other legal entities such as charities funded by government.
We anticipate a register needing to reference such entities using a "public-sector" field, a CURIE to one of a number of different registers.

# Lists

The data is being compiled from existing lists of organisations found in government data:

| List | Source |
| :---         |    :--- |
|[govuk](lists/govuk) |[GOV.UK government organisations](https://www.gov.uk/government/organisations)|
|[data-govuk](lists/data-govuk) |[data.gov.uk publishers](https://data.gov.uk/publisher)|
|[data-govuk-orgs](lists/data-govuk-orgs) |[data.gov.uk organisations](https://data.gov.uk)|
|[public-bodies-2013](lists/public-bodies-2013) |[Cabinet Office list of public bodies (2013)](https://www.gov.uk/government/publications/public-bodies-2013)|
|[public-bodies-2014](lists/public-bodies-2014) |[Cabinet Office list of public bodies (2014)](https://www.gov.uk/government/publications/public-bodies-2014)|
|[public-bodies-2015](lists/public-bodies-2015) |[Cabinet Office list of public bodies (2015)](https://www.gov.uk/government/publications/public-bodies-2015)|
|[public-bodies-2016](lists/public-bodies-2016) |[Cabinet Office list of public bodies (2016)](https://www.gov.uk/government/publications/public-bodies-2016)|
|[designation-of-public-bodies](lists/designation-of-public-bodies) |[Whole of Government Accounts (Designation of Bodies) Order 2015](http://www.legislation.gov.uk/uksi/2015/1655/made)|
|[whole-of-government-accounts](lists/whole-of-government-accounts) |[Whole of Government Accounts (PDF report)](https://www.gov.uk/government/collections/whole-of-government-accounts)|
|[ons-public-sector-classification](lists/ons-public-sector-classification) |[ONS Public Sector Classification Guide](https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/datasets/publicsectorclassificationguide)|
|[crown-bodies](lists/crown-bodies) |[The National Archives list of crown bodies](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/uk-crown-bodies/)|
|[coins](lists/coins) |[Combined Online Information System (COINS) organisations](https://www.whatdotheyknow.com/cy/request/list_of_public_bodies_in_the_coi#incoming-69457)|
|[oscar](lists/oscar) |[The Online System for Central Accounting and Reporting (OSCAR)](https://www.gov.uk/government/collections/hmt-oscar-publishing-from-the-database)|
|[cloudstore-buyers](lists/cloudstore-buyers) |[Public Sector organisations eligible to use cloudstore](https://www.gov.uk/government/publications/public-sector-organisations-eligible-to-use-cloudstore)|
|[miso](lists/miso) |[Crown Commercial Service management information system online](https://www.gov.uk/guidance/current-crown-commercial-service-suppliers-what-you-need-to-know)|
|[epims](lists/epims) |[Government property finder](https://www.epims.ogc.gov.uk/government-property-finder/home.aspx)|
|[civil-service-jobs](lists/civil-service-jobs) |[Civil service job index](https://www.civilservicejobs.service.gov.uk/csr/index.cgi)|
|[contracts-finder](lists/contracts-finder) |[Contracts finder notices](https://www.contractsfinder.service.gov.uk/Notice/Summary)|
|[contracts-finder-archive](lists/contracts-finder-archive) |[Contracts finder archive](https://data.gov.uk/data/contracts-finder-archive/data-feeds/)|


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
