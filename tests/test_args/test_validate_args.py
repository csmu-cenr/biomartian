import pytest

import pandas as pd


from utils.unit_test_helpers import StringIO

from args.validate_args import validate_column_list_lengths

def describe_validate_column_list_lengths():

    def test_with_too_few_intypes():
        with pytest.raises(ValueError):
            validate_column_list_lengths("0,1,4", "gene,chromo", "mirna mirna2 mirna3")

    def test_with_too_few_outtypes():
        with pytest.raises(ValueError):
            validate_column_list_lengths("0,1,4", "gene,chromo,whatevz", "mirna mirna2")


@pytest.fixture
def validate_args():
    {'--datasets': False,
     '--examples': False,
     '--issues': False,
     '--kinds': False,
     '--marts': False,
     '--website': False,
     '-c': ['0'],
     '-d': 'hsapiens_gene_ensembl',
     '-i': [],
     '-m': 'ensembl',
     '-n': 0,
     'FILE': None,
     'OUTTYPE': []}
