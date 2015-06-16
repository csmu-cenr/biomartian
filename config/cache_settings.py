from os.path import dirname, realpath, join as path_join
import logging

from joblib import Memory

biomart_config_path = dirname(realpath(__file__))
biomart_path_list = biomart_config_path.split("/")[:-1]
biomart_path = "/".join(biomart_path_list) + "/"
default_cache_path = path_join(biomart_path, "cache")

def set_up_caching(cachedir=default_cache_path, verbose=0):

    logging.debug("Using cache path:" + cachedir)

    memory = Memory(cachedir=cachedir, verbose=verbose)

    return memory


memory = set_up_caching(default_cache_path)
