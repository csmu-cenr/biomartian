from get_data.query_bm import get_bm
from get_data.query_other import get_other

from config.other_types import other_data_df

def get_data(intype, outtype, dataset, mart):

    if intype in other:
        get_other(intype, outtype, dataset, mart)
    else:
        query_bm(intype, outtype, dataset, mart)
