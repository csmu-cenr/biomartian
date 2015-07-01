import pytest

from biomartian.format_output.find_outcolumn_order import _correct_outpositions, _find_outindexes
from biomartian.format_output.find_outcolumn_order import get_final_outcolumn_order


def test__correct_outpositions():

    outindexes = [3, 5, 7]

    expected_result = [3, 6, 9]

    actual_result = _correct_outpositions(outindexes)

    assert expected_result == actual_result


def test_find__outindexes():

    header = 'Gene	logFC	AveExpr	t	P.Value	adj.P.Val	B	go_id'.split()

    merge_on_cols = ['t', 'B']

    actual_result = _find_outindexes(header, merge_on_cols)

    expected_result = [3, 6]

    assert actual_result == expected_result


def describe_get_final_outcolumn_order():

    def test_with_no_outindexes():

        header = 'Gene	logFC	AveExpr	t	P.Value	adj.P.Val	B	go_id'.split()
        merge_on_cols = ['Gene', "t"]

        actual_result = get_final_outcolumn_order([], header, merge_on_cols)

        expected_result = 'Gene  B	logFC	AveExpr	t  go_id	P.Value	adj.P.Val'.split()

        assert actual_result == expected_result


    def test_with_outindexes():

        header = 'Gene	logFC	AveExpr	t	P.Value	adj.P.Val	B	go_id'.split()
        outindexes = [2, 4]

        actual_result = get_final_outcolumn_order(outindexes, header, [])

        expected_result = 'Gene  logFC  B	AveExpr	t  go_id 	P.Value	adj.P.Val'.split()

        print(actual_result, "actual")
        print(expected_result, "expected")

        assert actual_result == expected_result
