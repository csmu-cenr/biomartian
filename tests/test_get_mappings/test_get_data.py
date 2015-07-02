import pytest

import pandas as pd

from biomartian.utils.unit_test_helpers import StringIO
from biomartian.get_mappings.get_data import is_requested_data_nonbm


def describe_is_requested_data_nonbm():

    def says_yes_to_nonbm_data(tables_that_exist):

        assert is_requested_data_nonbm("go_db", "gene_ontology", "term",
                                       tables_that_exist)

    def says_no_to_not_in_nonbm(tables_that_exist):

        assert not is_requested_data_nonbm("reactome_db", "reactome", "definisjon",
                                           tables_that_exist)



@pytest.fixture
def tables_that_exist():

    return pd.read_table(StringIO(u"mart   dataset   attribute\n"
                                  u"go_db  gene_ontology  term\n"
                                  u"go_db  gene_ontology  ontology\n"
                                  u"go_db  gene_ontology  definition\n"
                                  u"reactome_db  reactome  definition\n"),
                         sep="\s+")
