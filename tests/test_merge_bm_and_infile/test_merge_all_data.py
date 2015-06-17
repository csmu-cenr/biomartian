import pytest

import pandas as pd

from utils.unit_test_helpers import StringIO

from merge_bm_and_infile.merge_bm_infile import attach_all_columns

def test_attach_all_columns(in_df, column_df_map, expected_result):

    actual_result = attach_all_columns(in_df, column_df_map)
    assert actual_result.equals(expected_result)


@pytest.fixture
def column_df_map(go_map_df, moo_map_df):

    return {("Gene", "external_gene_name"): go_map_df, (0, "niniNI"): moo_map_df}


@pytest.fixture
def go_map_df():
    return pd.read_table(StringIO(u"""external_gene_name    GO_id
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
def moo_map_df():

    return pd.read_table(StringIO(u"""niniNI    Moo
    Madd    moo2
    Zmiz1   moo3
    Mt-nd1  moo1
    Cdca7   moo4"""), sep="\s+")


@pytest.fixture
def in_df():

    return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada
    Mt-nd1  1    5
    Madd    1    5
    Zmiz1   1    4
    Cdca7   2    3"""), sep="\s+")

@pytest.fixture
def expected_result():

    return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada    Moo    GO_id
    Mt-nd1  1    5      moo1     GO:0005739
    Mt-nd1  1    5      moo1     GO:0005743
    Mt-nd1  1    5      moo1     GO:0016021
    Madd    1    5      moo2     GO:0016021
    Madd    1    5      moo2     GO:0045202
    Madd    1    5      moo2     GO:0005886
    Zmiz1   1    4      moo3     GO:0043231
    Cdca7   2    3      moo4     GO:0005622
    Cdca7   2    3      moo4     GO:0005654"""), sep="\s+")
