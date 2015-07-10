"""bm

For help and examples, visit github.com/endrebak/biomartian

Usage:
    bm [--mart=MART] [--dataset=DATA] --mergecol=COL... --intype=IN... --outtype=OUT... [--noheader] FILE
    bm --list-marts
    bm [--mart=MART] --list-datasets
    bm [--mart=MART] [--dataset=DATASET] --list-attributes

Arguments:
    FILE                   file with COL(s) to join mart data on (- for STDIN)
    -i IN --intype=IN     the datatype in the column to merge on
    -o OUT --outtype=OUT   the datatype to get (joining on value COL)
    -c COL --mergecol=COL  name or number of the column to join on in FILE

Note:
    Required args --intype, --outtype and --mergecol must be equal in number.

Options:
    -h      --help          show this message
    -m MART --mart=MART     which mart to use [default: ensembl]
    -d DATA --dataset=DATA  which dataset to use [default: hsapiens_gene_ensembl]
    -n --noheader           the input data does not contain a header (must
                            use integers to denote COL)

Lists:
    --list-marts       show all available marts
    --list-datasets    show all available datasets for MART
    --list-attributes  show all kinds of data available for MART and DATASET
"""

from __future__ import print_function

from docopt import docopt
import sys

def list_bm_info(list_marts, list_datasets, list_attributes, mart, dataset):

    if list_marts:
        lists = get_marts()
    if list_datasets:
        lists = get_datasets(mart)
    if list_attributes:
        lists = get_attributes(mart, dataset)

    lists.to_csv(sys.stdout, sep="\t", index=False)
    sys.exit()

def append_data_to_infile(in_df, mergecols, intypes, outtypes, dataset, mart):

    for column, intype, outtype in zip(mergecols, intypes, outtypes):

        # sorting to ensure caching is triggered at every opportunity
        # (get_data produces a bi-directional map so order does not matter)
        sorted_intype, sorted_outtype = sorted([intype, outtype])

        intype_outtype_df = get_bm(sorted_intype, sorted_outtype, dataset, mart)
        in_df = attach_data(in_df, intype_outtype_df, column, intype)

    return in_df

if __name__ == "__main__":

    print("""
 _     _                            _   _
| |__ (_) ___  _ __ ___   __ _ _ __| |_(_) __ _ _ __
| '_ \| |/ _ \| '_ ` _ \ / _` | '__| __| |/ _` | '_ \\
| |_) | | (_) | | | | | | (_| | |  | |_| | (_| | | | |
|_.__/|_|\___/|_| |_| |_|\__,_|_|   \__|_|\__,_|_| |_|
                   Query biomart from the command line
""",
          file=sys.stderr)

    args = docopt(__doc__, help=True)

    from ebs.read_indata import read_indata
    from ebs.args import turn_docopt_arg_names_into_valid_var_names
    from ebs.merge_cols import attach_data

    from biomartian.args.validate_args import validate_args
    from biomartian.r.r import get_marts, get_datasets, get_attributes, get_bm

    args = turn_docopt_arg_names_into_valid_var_names(args)
    # load cl-args into local namespace # pylint: disable=E0602
    locals().update(args)

    if list_marts or list_datasets or list_attributes:
        list_bm_info(list_marts, list_datasets, list_attributes, mart, dataset)

    validate_args(args)

    in_df = read_indata(args["FILE"], False)

    in_df = append_data_to_infile(in_df, mergecol, intype, outtype, dataset,
                                  mart)

    in_df.head().to_csv(sys.stdout, sep="\t", index=False, na_rep="NA")
