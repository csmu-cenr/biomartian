import pytest

import pandas as pd

from utils.unit_test_helpers import StringIO

from merge_bm_and_infile.add_col import get_column_to_merge_on

def describe_get_column_to_merge_on():

    def test_with_name(in_df):

        assert "Gene" == get_column_to_merge_on(in_df.columns, "Gene")

    def test_with_int(in_df):

        assert "Gene" == get_column_to_merge_on(in_df.columns, 0)


    def test_with_strin_int(in_df):

        assert "Gene" == get_column_to_merge_on(in_df.columns, "0")

@pytest.fixture
def map_df():
    return pd.read_table(StringIO(u"""Gene    Term
    Mt-nd1  GO:0005739
    Mt-nd1  GO:0005743
    Mt-nd1  GO:0016021
    Madd    GO:0016021
    Madd    GO:0045202
    Madd    GO:0005886
    Zmiz1   GO:0043231
    Cdca7   GO:0005622
    Cdca7   GO:0005654"""), sep="\s+")

@pytest.fixture
def in_df():

    return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada
    Mt-nd1  1    5
    Madd    1    5
    Zmiz1   1    4
    Cdca7   2    3"""), sep="\s+")

@pytest.fixture
def expected_result():

    return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada    Term
    Mt-nd1  1    5     GO:0005739
    Mt-nd1  1    5     GO:0005743
    Mt-nd1  1    5     GO:0016021
    Madd    1    5     GO:0016021
    Madd    1    5     GO:0045202
    Madd    1    5     GO:0005886
    Zmiz1   1    4     GO:0043231
    Cdca7   2    3     GO:0005622
    Cdca7   2    3     GO:0005654 """), sep="\s+")
