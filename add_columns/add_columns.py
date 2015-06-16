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


# def convert_r_string_to_df(df_string):

#     assert df_string, "dataframe empty"
#     # Hack because I've had some problems with pyper
#     # The API is just r_session.get("df_name")

#     try: # python3
#         df_as_string = StringIO(df_string)
#     except: # python2
#         df_as_string = StringIO(unicode(df_string, "utf-8"))

#     df = pd.read_table(df_as_string,
#                        skiprows=[0, 1], usecols=[1,2],
#                        header=None, sep="\s+", dtype=str).dropna(how="any")

#     return df


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


def get_column_to_merge_on(in_df_columns, merge_on_int_or_string):
    """Users can use both an int or a name to choose columns.

    This method takes care of the conversions."""

    try:
        merge_on = list(in_df_columns)[merge_on_int_or_string]
    except TypeError: # merge on was already a string
        merge_on = merge_on_int_or_string

    return merge_on


def attach_columns(in_df, map_df, merge_on, outtype, non_long):

    # change the intype to "index": hack, should only be done when no header?
    map_df.columns = [col if col == outtype else "index" for col in map_df.columns]

    logging.debug("Merging:\n" + str(in_df.head()))
    logging.debug("And:\n" + str(map_df.head()))
    logging.debug("On:\n" + merge_on)

    relevant_maps = map_df[map_df[merge_on].isin(in_df[merge_on])].dropna()
    if not non_long:
        in_df = in_df.merge(relevant_maps, on=merge_on, how="outer").dropna().drop_duplicates()
    else:
        d = {k: ",".join(g[outtype].tolist()) for k, g in relevant_maps.groupby(merge_on)}
        col = in_df[merge_on].map(d)
        in_df.insert(len(in_df.columns), outtype, col)

    return in_df
