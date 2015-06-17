import pytest

import pandas as pd

from utils.unit_test_helpers import StringIO

from biomart.query_bm import perform_all_queries

"Ensure that intype outtype df map does not contain equal keys; happened once due to sorting."

# @pytest.mark.integration
# def describe_perform_all_queries():

    # actual_result = perform_all_queries("rnorvegicus_gene_ensembl", "ensembl", intype_outtype_dict)

    # def test_keys_in_output(intype_outtype_dict):
        # actual_result = perform_all_queries("rnorvegicus_gene_ensembl", "ensembl", intype_outtype_dict)
        # assert list(actual_result) == [{"external_gene_name": "entrezgene"}]


    # def test_type_in_output(intype_outtype_dict):
        # actual_result = perform_all_queries("rnorvegicus_gene_ensembl", "ensembl", intype_outtype_dict)
        # first_result = list(actual_result.values())[0]
        # assert type(first_result) == pd.core.frame.DataFrame

@pytest.fixture
def intype_outtype_dict():
    return {"external_gene_name": "entrezgene"}

@pytest.fixture
def expected_result():
    return {"external_gene_name": "entrezgene"}
