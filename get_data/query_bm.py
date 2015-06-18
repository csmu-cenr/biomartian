from os.path import dirname, join as path_join
from subprocess import call
import logging
from collections import defaultdict

import pandas as pd

from r.r import set_up_mart

from config.cache_settings import memory, default_cache_path
from config.logging_settings import set_up_logging

set_up_logging(logging.DEBUG)

@memory.cache(verbose=0)
def get_bm(intype, outtype, dataset, mart, cache_directory=default_cache_path):

    """Queries biomart for data.

    Gets the whole map between INTYPE <-> OUTTYPE and caches it so that disk based
    lookups are used afterwards."""

    r = set_up_mart(mart, dataset)

    get_command = """

    input_output_map_df <- getBM(attributes=c('{input_type}',
    '{output_type}'), mart = mart, values = '*')

    """.format(input_type=intype, output_type=outtype)

    print(get_command)
    r.call(get_command)

    outfile = get_data_output_filename(intype, outtype, dataset, mart, cache_directory)

    write_command = """

    write.table(input_output_map_df, '{}', sep='\t', row.names=F)

    """.format(outfile)

    print(write_command)
    r.call(write_command)

    map_df = pd.read_table(outfile, header=0, dtype=str)

    return map_df


def get_data_output_filename(intype, outtype, dataset, mart, default_cache_path):

    """Stores a human readable file of biomart query results."""

    filename = "_".join([intype, outtype, dataset, mart]) + ".txt"

    path_name = path_join(default_cache_path, "human_readable")

    call("mkdir -p {}".format(path_name), shell=True)

    outfile = path_join(path_name, filename)

    return outfile
