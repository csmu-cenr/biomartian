import pytest

import pandas as pd

from biomartian.lists.get_lists import get_non_bm_attributes, get_non_bm

from biomartian.utils.unit_test_helpers import StringIO


def describe_get_attributes():

    def gets_correct_attributes(dataset_file):

        actual_result = get_non_bm_attributes(dataset_file)
        expected_result = ["ontology", "term"]

        assert actual_result == expected_result


@pytest.fixture
def dataset_file(tmpdir):

    attr_file = tmpdir.join("dataset.py")

    attr_file.write("from biomartian.non_biomarts.go_db.get_go_data.get_go import get_go_map\n"
                    "\n"
                    "def get_ontology():\n"
                    "    return get_go_map('ontology')\n"
                    "\n"
                    "def get_term():\n"
                    "    return get_go_map('term')\n")

    return str(attr_file)


def describe_get_marts():

    def gets_correct_marts(expected_result):

        extensions_folder = "tests/test_lists/integration_test_folder/"
        actual_result = get_non_bm(extensions_folder)

        # code below sorts the dfs and creates the index anew to ensure the dfs are
        # equal
        expected_result = expected_result.sort("attribute").reset_index(drop=True)
        actual_result = actual_result.sort("attribute").reset_index(drop=True)

        assert expected_result.equals(actual_result)

@pytest.fixture
def expected_result():

    return pd.read_table(StringIO(u"mart   dataset   attribute\n"
                                  u"go_db  gene_ontology  term\n"
                                  u"go_db  gene_ontology  ontology\n"
                                  u"go_db  gene_ontology  definition\n"
                                  u"reactome_db  reactome  definition\n"),
                         sep="\s+")
