from biomartian.get_mappings.query_bm import get_bm
from biomartian.get_mappings.query_other import get_other

from biomartian.config.cache_settings import memory


@memory.cache(verbose=0)
def get_data(intype, outtype, dataset, mart):

    if mart == "biomartian":
        return get_other(intype, outtype, dataset)
    else:
        return get_bm(intype, outtype, dataset, mart)
