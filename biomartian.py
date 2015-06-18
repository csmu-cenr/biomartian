"""biomartian

Query biomart from the command line.
For help and examples, visit github.com/endrebak/biomartian (biomartian --website)

Usage:
    biomartian [--mart=MART] [--dataset=DATASET] --column=COLUMN... --intype=INTYPE... --outtype=OUTTYPE... [--noheader] FILE
    biomartian --annotation=TYPE --column=COLUMN... [--outindex=INDEX...] FILE
    biomartian --list-marts
    biomartian -m MART --list-datasets
    biomartian -m MART -d DATASET [--list-kinds|--list-examples]
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
                               of the COLUMN, unless used with -k in which case it is
                               to the very right, due to the variable length of -k output)
    -a TYPE --definition=TYPE  add the definitions (annotations) of GOIDs or REACTOME terms
    -n --noheader              the input data does not contain a header (must use integer
                               indexing)
Lists:
    --list-marts     show all available marts
    --list-datasets  show all available datasets for MART
    --list-kinds     show all kinds of data available for MART and DATASET
    --list-examples  show examples of all kinds of data for MART and DATASET
    --list-annotations
Web:
    --website  visit github.com/endrebak/biomartian for more examples and docs
    --issues   visit the issues page for biomartian to ask questions, make suggestions or report bugs
"""


# Formatting:
#     --stackcol  if multiple stackcol rows per indexcol, merge them into comma-separated list indexcol:stackcol
# Annotation:
#     --add-annotation []
#

from docopt import docopt



if __name__ == "__main__":


    args = docopt(__doc__, help=True)

    # if args["--website"]:
        # webbrowser.open_new_tab("http://github.com/endrebak/biomartian")
    # if args["--issues"]:
        # webbrowser.open_new_tab("http://github.com/endrebak/biomartian/issues")
    # else:
        # delay loading so that help message screen shown instantaneously
    import sys
    from collections import defaultdict

    from args.validate_args import validate_args
    from args.parse_args import parse_args
    # from get_data.get_data import get_data
    from merge_bm_and_infile.add_col import attach_column
    from read_indata.read_indata import read_indata
    from config.other_data import other_data_df
    print(other_data_df)
    raise

    validate_args(args)

    in_df = read_indata(args["FILE"], False)
    columns, intypes, outtypes = args["--column"], args["--intype"], args["--outtype"]
    dataset, mart = args["--dataset"], args["--mart"]


    out_df = in_df

    for column, intype, outtype, outindex in zip(columns, intypes, outtypes, outindex):
        get_data(intype, outtype, dataset, mart) # if data not in other, look in mart
    # for column, intype, outtype in zip(columns, intypes, outtypes):
    #     intype_outtype_df = get_bm(intype, outtype, dataset, mart)
    #     out_df = attach_column(out_df, intype_outtype_df, column, intype)

    # for

    out_df.to_csv(sys.stdout, sep="\t", index=False)
