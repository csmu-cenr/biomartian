
import pandas as pd
from os.path import dirname, join as path_join
from importlib import import_module

from subprocess import call

from biomartian.config.cache_settings import default_cache_path, memory

from widediaper import R

def load_getter(mart, dataset, attribute, basefolder=""):
    print(basefolder)
    base_module = dirname(basefolder+"/").replace("/", ".")
    print(base_module)
    module = "{base_module}.{mart}.{dataset}".format(**locals())
    print(module)
    dataset_module = import_module(module)
    attribute_function = getattr(dataset_module,
                                 "get_{attribute}".format(attribute=attribute))

    return attribute_function


@memory.cache(verbose=0)
def get_other(outtype, dataset, mart):

    print("mart", mart, "dataset", dataset, "outtype", outtype)
    getter = load_getter(mart, dataset, outtype, "biomartian/non_biomarts")
    return getter()
