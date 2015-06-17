import pytest

import pandas as pd

from utils.unit_test_helpers import StringIO

from args.parse_args import parse_args

def describe_parse_args():


    def test_parse_outtypes(args):
        actual_result = parse_args(args)
        assert actual_result["--outtype"] == [["entrezgene", "mirna"], ["whatevz"]]


@pytest.fixture
def args():
    return {'--column': '0',
            '--columns': False,
            '--dataset': 'hsapiens_gene_ensembl',
            '--datasets': False,
            '--examples': False,
            '--intype': "1,2,3",
            '--issues': False,
            '--kinds': False,
            '--mart': 'ensembl',
            '--marts': False,
            '--noheader': False,
            '--outtype': "entrezgene,mirna whatevz",
            '--website': False,
            'FILE': None}
