import pytest

import pandas as pd
from numpy import array_equal

from biomartian.utils.unit_test_helpers import StringIO

from biomartian.merge_bm_and_infile.add_col import attach_column

def describe_attach_column():

    @pytest.fixture
    def map_df():
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
    def in_df():

        return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada
        Mt-nd1  1    5
        Madd    1    5
        Zmiz1   1    4
        Cdca7   2    3"""), sep="\s+")

    @pytest.fixture
    def expected_result():

        return pd.read_table(StringIO(u"""Gene    Blabla   Yadayada    GO_id
        Mt-nd1  1    5     GO:0005739
        Mt-nd1  1    5     GO:0005743
        Mt-nd1  1    5     GO:0016021
        Madd    1    5     GO:0016021
        Madd    1    5     GO:0045202
        Madd    1    5     GO:0005886
        Zmiz1   1    4     GO:0043231
        Cdca7   2    3     GO:0005622
        Cdca7   2    3     GO:0005654 """), sep="\s+")

    def test_attach_with_name(in_df, map_df, expected_result):

        actual_result = attach_column(in_df, map_df, "Gene", "external_gene_name")

        assert array_equal(actual_result, expected_result)


    def test_attach_with_int(in_df, map_df, expected_result):

        print(expected_result)

        actual_result = attach_column(in_df, map_df, 0, "external_gene_name")

        print(actual_result)

        assert array_equal(actual_result, expected_result)

    ###

    @pytest.fixture
    def in_df_with_intype_as_col():

        return pd.read_table(StringIO((u"Gene    Blabla   Yadayada    GO_id\n"
                                    "Mt-nd1  1    5     GO:0005739\n"
                                    "Mt-nd1  1    5     GO:0005743\n"
                                    "Mt-nd1  1    5     GO:0016021\n"
                                    "Madd    1    5     GO:0016021\n"
                                    "Madd    1    5     GO:0045202\n"
                                    "Madd    1    5     GO:0005886\n"
                                    "Zmiz1   1    4     GO:0043231\n"
                                    "Cdca7   2    3     GO:0005622\n"
                                    "Cdca7   2    3     GO:0005654")), sep="\s+")

    @pytest.fixture
    def map_df_with_intype_as_col():

        return pd.read_table(StringIO((u"entrezgene    GO_id\n"
                                    "1742   GO:0005739\n"
                                    "1742   GO:0005743\n"
                                    "1742   GO:0016021\n"
                                    "7331   GO:0045202\n"
                                    "7331   GO:0005886\n"
                                    "42     GO:0043231\n"
                                    "1881   GO:0005622\n"
                                    "1881   GO:0005654")), sep="\s+")

    @pytest.fixture
    def expected_result_with_intype_as_col():

        return pd.read_table(StringIO((u"Gene    Blabla   Yadayada    GO_id    entrezgene\n"
                                    "Mt-nd1  1    5     GO:0005739    1742\n"
                                    "Mt-nd1  1    5     GO:0005743    1742\n"
                                    "Mt-nd1  1    5     GO:0016021    1742\n"
                                    "Madd    1    5     GO:0016021    1742\n"
                                    "Madd    1    5     GO:0045202    7331\n"
                                    "Madd    1    5     GO:0005886    7331\n"
                                    "Zmiz1   1    4     GO:0043231    42  \n"
                                    "Cdca7   2    3     GO:0005622    1881\n"
                                    "Cdca7   2    3     GO:0005654    1881")), sep="\s+")


    def test_attach_when_intype_exists_as_col_in_df(in_df_with_intype_as_col,
                                                    map_df_with_intype_as_col,
                                                    expected_result_with_intype_as_col):

        actual_result = attach_column(in_df_with_intype_as_col, map_df_with_intype_as_col, "GO_id", "GO_id")

        assert array_equal(actual_result, expected_result_with_intype_as_col)
