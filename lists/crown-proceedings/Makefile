# see https://www.gov.uk/government/publications/serve-the-treasury-solicitor-with-legal-proceedings

cache/data.pdf:
	mkdir -p cache
	curl -qs 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/595199/The_Crown_Proceedings_Act_1947_-_List_of_Authorised_Departments_and_Solicitors_for_Service_30_January_2017.pdf' > $@


clean::
	rm -rf cache
