import pytest

import pandas as pd


from utils.unit_test_helpers import StringIO

from args.validate_args import validate_args

def describe_validate_column_list_lengths():

    def test_with_valid_args(valid_args):
        validate_args(valid_args)

    def test_with_invalid_args(invalid_args):
        with pytest.raises(ValueError):
            validate_args(invalid_args)


@pytest.fixture
def valid_args():

    return {'--column': ['0', '0'],
            '--dataset': 'rnorvegicus_gene_ensembl',
            '--intype': ['external_gene_name', 'external_gene_name'],
            '--issues': False,
            '--list-columns': False,
            '--list-datasets': False,
            '--list-examples': False,
            '--list-kinds': False,
            '--list-marts': False,
            '--mart': 'ensembl',
            '--noheader': False,
            '--outtype': ['entrezgene', 'refseq_mrna'],
            '--website': False,
            'FILE': 'examples/test_file_full_header.txt'}

@pytest.fixture
def invalid_args():

    return {'--column': ['0', '0'],
            '--dataset': 'rnorvegicus_gene_ensembl',
            '--intype': ['external_gene_name'],
            '--issues': False,
            '--list-columns': False,
            '--list-datasets': False,
            '--list-examples': False,
            '--list-kinds': False,
            '--list-marts': False,
            '--mart': 'ensembl',
            '--noheader': False,
            '--outtype': ['entrezgene', 'refseq_mrna'],
            '--website': False,
            'FILE': 'examples/test_file_full_header.txt'}
