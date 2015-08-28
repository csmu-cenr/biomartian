#!/usr/bin/env python

from __future__ import print_function

from docopt import docopt
import sys
from numpy import equal, mod
import pandas as pd
from numpy import float64

from ebs.imports import StringIO
from ebs.read_indata import read_indata
from ebs.args import turn_docopt_arg_names_into_valid_var_names
from ebs.merge_cols import attach_data

from biomartian.args.validate_args import validate_args
from biomartian.bm_queries.bm_query import get_marts, get_datasets, get_attributes, get_bm

import warnings
warnings.filterwarnings("ignore")

def list_bm_info(list_marts, list_datasets, list_attributes, mart, dataset):
    if list_marts:
        lists = get_marts()
    if list_datasets:
        lists = get_datasets(mart)
    if list_attributes:
        lists = get_attributes(dataset)

    lists.to_csv(sys.stdout, sep="\t", index=False)
    sys.exit()


def append_data_to_infile(in_df, mergecols, intypes, outtypes, dataset, mart):

    for column, intype, outtype in zip(mergecols, intypes, outtypes):

        sorted_intype, sorted_outtype = _sort_args([intype, outtype])

        intype_outtype_df = get_bm(sorted_intype, sorted_outtype, dataset, mart)

        intype_outtype_df = _turn_int_cols_with_na_into_str(intype_outtype_df,
                                                            outtype)

        in_df = attach_data(in_df, intype_outtype_df, column, intype)

    return in_df

def _turn_int_cols_with_na_into_str(map_df, outtype):

    """Turn float cols that actually contain ints into strtype.

    Since there is no NaN for ints, intcols with NaNs are promoted to float.

    This is annoying when ints are a better fit, i.e. for years (1996.0). It is
    plain wrong when the int is a name, i.e. the "p53" gene is 1234 in some
    annotations, NOT 1234.0.

    To avoid such conversions, any 'int-float' columns are converted to strings.
    """

    outcol = map_df[outtype]

    is_float = issubclass(outcol.dtype.type, float)

    try:
        all_are_ints = all(equal(mod(outcol.dropna(), 1), 0))
    except TypeError:
        return map_df

    if is_float and all_are_ints:
        map_df[outtype] = map_df[outtype].astype(str).apply(
            lambda s: s.split(".")[0])

    return map_df


def _sort_args(args):

    """Sorting args before calling function to ensure cache is triggered at
    every opportunity."""

    return sorted(args)


def biomartian(mart='ensembl', dataset='hsapiens_gene_ensembl', noheader=False,
               list_marts=False, list_datasets=False, list_attributes=False,
               FILE=None, intype=None, outtype=None, mergecol=None):

    args = dict([(k, v) for k, v in locals().items() if k in ['mart', 'dataset',
                                                      'noheader', 'list_marts',
                                                      'list_datasets',
                                                      'list_attributes',
                                                      'FILE', 'intype',
                                                      'outtype', 'mergecol']])

    # just list data and exit
    if list_marts or list_datasets or list_attributes:
        list_bm_info(list_marts, list_datasets, list_attributes, mart, dataset)

    if intype is None or outtype is None:
        raise ValueError("Both intype and outtype must be specified")

    if not isinstance(intype, (list, tuple)):
        intype = [intype]

    if not isinstance(outtype, (list, tuple)):
        outtype = [outtype]

    # if infile given, append to infile and send result to stdout
    if FILE:
        validate_args(args)
        in_df = read_indata(FILE, noheader)
        result_df = append_data_to_infile(in_df, mergecol, intype, outtype, dataset,
                                  mart)
    # if no infile given just dump all data to stdout
    else:
        sorted_intype, sorted_outtype = _sort_args(intype + outtype)
        result_df = get_bm(sorted_intype, sorted_outtype, dataset, mart)

    return result_df
