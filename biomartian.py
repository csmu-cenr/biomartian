"""biomartian

For help and examples, visit github.com/endrebak/biomartian (biomartian --website)

Usage:
    biomartian [--mart=MART] [--dataset=DATASET] --column=COLUMN... --intype=INTYPE... --outtype=OUTTYPE... [--noheader] FILE
    biomartian --annotation=TYPE --column=COLUMN... [--outindex=INDEX...] FILE
    biomartian --list-marts
    biomartian [--mart=MART] --list-datasets
    biomartian [--mart=MART] [--dataset=DATASET] [--list-attributes|--list-examples]
    biomartian --list-columns FILE
    biomartian [--website|--issues]

Arguments:
    FILE  file with COLUMN(s) to join mart data on (supports piping)
    -i TYPE --intype=TYPE      the datatype in the column to merge on
    -o TYPE --outtype=TYPE     the datatype to get (joining on value COLUMN)
    -c COLUMN --column=COLUMN  name or number of the column to join on in FILE

Note:
    Required arguments --intype, --outtype and --column must be equal in number.
    (--outindex must either not be used or equal in number to the above.)

Options:
    -h --help                  show this message
    -m MART --mart=MART        which mart to use [default: ensembl]
    -d DATA --dataset=DATA     which dataset to use [default: hsapiens_gene_ensembl]
    -x INDEX --outindex=INDEX  index at which to place the data (by default to the right
                               of the COLUMN)
    -a TYPE --definition=TYPE  add the definitions (annotations) of GOIDs or REACTOME terms
    -n --noheader              the input data does not contain a header (must use integers
                               to denote COLUMN)
Lists:
    --list-marts     show all available marts
    --list-datasets  show all available datasets for MART
    --list-kinds     show all kinds of data available for MART and DATASET
    --list-examples  show examples of all kinds of data for MART and DATASET
Web:
    --website     visit github.com/endrebak/biomartian for more examples and docs
    --phone-home  ask questions, make suggestions or report bugs at the biomartian issues page
"""

# refactor so that modules in biomartian/

# listmarts
# Ensure reactome works with data
# get output columns in the correct order
# Formatting:
#     --stackcol  if multiple stackcol rows per indexcol, merge them into comma-separated list indexcol:stackcol
#                 this makes the data unsuitable for most downstream analysis (cf. Wickham's "Tidy Data")
#     --transpose
#     --na-symbol [default: NA]
#     --drop-na
#     --delim-col  [default: "\t"]
#     --delim-stack [default: ,]
# Cache:
#     --view-dates
#     --cache-delete
# Helpers:
#     --view-in-colnb
#     --view-out-colnb
#     --r-packages
# --Other
# Create examples in example-file folder
# ensure that in and out-data are never the same
from __future__ import print_function

from docopt import docopt
import sys

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

    from biomartian.args.validate_args import validate_args
    from biomartian.get_mappings.get_data import get_data
    from biomartian.merge_bm_and_infile.add_col import attach_column
    from biomartian.read_indata.read_indata import read_indata
    from biomartian.config.other_data import other_data_df
    from biomartian.lists.get_lists import get_marts#, get_datasets
    # from biomartian.lists.get_lists import get_attributes

    validate_args(args)
    columns, intypes, outtypes = args["--column"], args["--intype"
                                                        ], args["--outtype"]
    dataset, mart = args["--dataset"], args["--mart"]

    if args["--list-marts"]:
        marts = get_marts()
        marts.to_csv(sys.stdout, sep="\t", index=False)
        sys.exit()
    if args["--list-datasets"]:
        datasets = get_datasets(mart)
        datasets.to_csv(sys.stdout, sep="\t", index=False)
        sys.exit()
    if args["--list-attributes"]:
        attributes = get_attributes(mart, dataset)
        attributes.to_csv(sys.stdout, sep="\t", index=False)
        sys.exit()

    in_df = read_indata(args["FILE"], False)

    out_df = in_df.copy()

    for column, intype, outtype in zip(columns, intypes, outtypes):

        # sorting to ensure caching is triggered at every opportunity
        # (get_data produces a bi-directional map so order does not matter)
        ordered_intype, ordered_outtype = sorted([intype, outtype])

        intype_outtype_df = get_data(ordered_intype, ordered_outtype, dataset,
                                     mart)
        out_df = attach_column(out_df, intype_outtype_df, column, intype)

    # if args["--website"]:
    # webbrowser.open_new_tab("http://github.com/endrebak/biomartian")
    # if args["--issues"]:
    # webbrowser.open_new_tab("http://github.com/endrebak/biomartian/issues")
    # else:
    # delay loading so that help message screen shown instantaneously

    # out_df.to_csv(sys.stdout, sep="\t", index=False)
