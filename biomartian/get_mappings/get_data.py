from biomartian.get_mappings.query_bm import get_bm
from numpy import array
from biomartian.get_mappings.query_other import get_other

from biomartian.config.cache_settings import memory
from biomartian.lists.get_lists import get_non_bm


@memory.cache(verbose=0)
def get_data(intype, outtype, dataset, mart):

    if is_requested_data_nonbm(mart, dataset, outtype):
        return get_other(outtype, dataset, mart)
    else:
        return get_bm(intype, outtype, dataset, mart)


def is_requested_data_nonbm(mart, dataset, attribute, lookup=None):

    if lookup is None:
        lookup = get_non_bm()

    return (lookup == array([mart, dataset, attribute])).all(1).any()
