import pytest

import pandas as pd


from biomartian.utils.unit_test_helpers import StringIO

from biomartian.args.validate_args import validate_same_number_of_args

from biomartian.args.validate_args import validate_outindexes_must_be_same_length_if_used

def describe_validate_same_number_of_args():

    def test_with_valid_args(valid_args):
        validate_same_number_of_args(valid_args)

    def test_with_invalid_args_too_few_intypes(invalid_args_too_few_intypes):
        with pytest.raises(ValueError):
            validate_same_number_of_args(invalid_args_too_few_intypes)

    @pytest.fixture
    def valid_args():
        return {'--column': ['0', '0'],
                '--intype': ['external_gene_name', 'external_gene_name'],
                '--outindex': [2],
                '--outtype': ['entrezgene', 'refseq_mrna'],}

    @pytest.fixture
    def invalid_args_too_few_intypes():

        return {'--column': ['0', '0'],
                '--intype': ['external_gene_name'],
                '--outindex': [2],
                '--outtype': ['entrezgene', 'refseq_mrna'],}

def describe_validate_outindexes_must_be_same_length_if_used():

    def test_with_invalid_args_too_few_outindexes(invalid_args_too_few_outindexes):
        with pytest.raises(ValueError):
            validate_outindexes_must_be_same_length_if_used(invalid_args_too_few_outindexes)

    @pytest.fixture
    def invalid_args_too_few_outindexes():
        return {'--column': ['0', '0'],
                '--intype': ['external_gene_name', 'external_gene_name'],
                '--outindex': [2],
                '--outtype': ['entrezgene', 'refseq_mrna'],}
