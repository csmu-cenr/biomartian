import pytest

from biomartian.get_mappings.query_other import load_getter




def describe_get_other_mappings():

    def is_able_to_import_modules_dynamically():
        # this test just checks whether we are able to load a module
        # dynamically (it tries to fetch a function that returns 45-42)
        # hence, getter() == 3 asserts that all is well.

        getter = load_getter("reactome_db", "reactome", "definition",
                             "tests/test_lists/integration_test_folder/")
        assert getter() == 3
