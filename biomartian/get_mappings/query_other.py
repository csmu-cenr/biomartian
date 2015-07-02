
import pandas as pd
from os.path import dirname, join as path_join
from importlib import import_module

from subprocess import call

from biomartian.config.cache_settings import default_cache_path, memory

from widediaper import R

def load_getter(mart, dataset, attribute, basefolder=""):
    base_module = dirname(basefolder).replace("/", ".")
    module = "{base_module}.{mart}.{dataset}".format(**locals())
    dataset_module = import_module(module)
    attribute_function = getattr(dataset_module,
                                 "get_{attribute}".format(attribute=attribute))

    return attribute_function


def get_other(outtype, dataset, mart):

    getter = load_getter(mart, dataset, outtype, "biomartian/non_biomart")
    return getter()
