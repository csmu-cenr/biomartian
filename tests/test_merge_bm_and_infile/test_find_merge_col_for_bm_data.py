import pytest

from collections import defaultdict

from merge_bm_and_infile.merge_bm_infile import convert_in_out_map_to_merge_in_map


def test_convert_in_out_map_to_merge_in_map(expected_result, intype_outtype_map, merge_cols, intypes, outtypes):

    actual_result = convert_in_out_map_to_merge_in_map(intype_outtype_map, merge_cols, intypes, outtypes)
    assert sorted(actual_result) == sorted(expected_result)

@pytest.fixture
def expected_result():

    return defaultdict(list, {("col1", "gene_type1"): ["df1", "df2"], ("Gene", "gene_type2"): ["df3"]})

@pytest.fixture
def intype_outtype_map():
    return {("gene_type1", "gene_type_1337"): "df1", ("gene_type1", "gene_type42"): "df2",
            ("gene_type2", "gene_type50"): "df3"}

@pytest.fixture
def merge_cols():
    return ["col1", "Gene"]

@pytest.fixture
def intypes():
    return ["gene_type1", "gene_type2"]

@pytest.fixture
def outtypes():
    return [["gene_type_1337", "gene_type42"], ["gene_type50"]]
