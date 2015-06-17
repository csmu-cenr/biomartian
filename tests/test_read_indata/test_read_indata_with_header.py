import pytest
import pandas as pd

from read_indata.read_indata import read_indata
from utils.unit_test_helpers import format_df_string, StringIO

def test_read_indata_with_header(df_header, expected_result_header):

    actual_result = read_indata(df_header, False)

    if not actual_result.equals(expected_result_header):
        print(actual_result, "ACTUAL")
        print(expected_result_header, "EXPECTED")

    assert actual_result.equals(expected_result_header)

DF_STRING = format_df_string(u"""Gene    Fold   LogCPM
                            "Ipcef1"	-2.70987558746701	4.80047582653889
                            "Sema3b"	2.00143465979322	3.82969788437155
                            "Lcat"	2.11219348292396	3.16122865097382""")
@pytest.fixture
def df_header():

    return StringIO(DF_STRING)

@pytest.fixture
def expected_result_header():

    df = pd.read_table(StringIO(DF_STRING), header=0, dtype=str, sep="\s+")

    return df
