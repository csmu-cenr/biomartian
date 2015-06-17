from datetime import datetime
import sys
import logging
from os.path import join as path_join
from subprocess import call

import pandas as pd

from config.cache_settings import memory, default_cache_path
import config.logging_settings

config.logging_settings.set_up_logging(logging.DEBUG)

from r.r import set_up_mart

try: # python3
    from io import StringIO
except ImportError: # python2
    from StringIO import StringIO


def get_timestamped_data(intype, outtype, dataset, mart):

    map_tuple = tuple(sorted([intype, outtype]))

    return _get_timestamped_data(map_tuple, dataset, mart)


@memory.cache()
def _get_timestamped_data(in_out_tuple, dataset, mart):

    intype, outtype = in_out_tuple

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = _get_data(intype, outtype, dataset, mart)

    data.columns = [intype, outtype]

    return timestamp, data


def _get_data(intype, outtype, dataset, mart):

    r = set_up_mart(mart, dataset)

    command = "input_output_map_df <- getBM(attributes=c('{input_type}'," \
              " '{output_type}'), mart = mart, values = '*')" \
                  .format(input_type=intype, output_type=outtype)

    logging.info("Querying biomart {} ({}) for {} to {} map." \
                 .format(mart, dataset, intype, outtype))
    logging.debug("Query command used: " + command)
    r.call(command)
    logging.debug("First 50 lines from mart look like: "\
                  + r.call("head(input_output_map_df, n = 50)"))

    filename = "_".join([intype, outtype, dataset]) + ".txt"
    path_name = path_join(default_cache_path, "human_readable")
    call("mkdir -p {}".format(path_name), shell=True)
    outfile = path_join(path_name, filename)

    logging.debug("Getting created mapping.")
    write_command = "write.table(input_output_map_df, '{}', sep='\t', row.names=F)".format(outfile)

    r.call("nrow(input_output_map_df)")
    logging.debug(write_command)
    r.call(write_command)
    logging.debug("Done")


    map_df = pd.read_table(outfile, header=0, dtype=str)

    return map_df


def add_columns(in_df, dataset, mart, additions_to_make):

    output_positions, timestamps = [], []
    for intype, additions in additions_to_make.items():

        out_types = additions["out_types"]
        insert_positions = additions["insert_positions"]
        merge_on = additions["merge_on"]
        non_long_cols = additions["non_long"]

        for outtype, insert_position in zip(out_types, insert_positions):
            timestamp, map_df = get_timestamped_data(intype, outtype, dataset, mart)
            timestamps.append((intype, outtype, timestamp))

            merge_on = get_column_to_merge_on(in_df.columns, merge_on)

            non_long = True if outtype in non_long_cols else False
            in_df = attach_columns(in_df, map_df, merge_on, outtype, non_long)


            logging.debug("Trying to merge on '{}'".format(merge_on))

    return in_df, timestamps
