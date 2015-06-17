"""biomartian

Query biomart from the command line.
For help and examples, visit github.com/endrebak/biomartian (biomartian --website)

Usage:
    biomartian [--mart=MART] [--dataset=DATASET] --column=COLUMN --intype=INTYPE --outtype=OUTTYPE [--noheader] FILE
    biomartian --list-marts
    biomartian -m MART --list-datasets
    biomartian -m MART -d DATASET [--list-kinds|--list-examples]
    biomartian --list-columns FILE
    biomartian [--website|--issues]

Arguments:
    FILE  file with COLUMN(s) to join mart data on

Options:
    -h --help                     show this message
    -m MART --mart=MART           which mart to use [default: ensembl]
    -d DATASET --dataset=DATASET  which dataset to use [default: hsapiens_gene_ensembl]
    -c COLUMN --column=COLUMN     name or number of the column to join on in FILE (comma-separated)
    -i INTYPE --intype=INTYPE     the datatype in the column to merge on (comma-separated, must have length equal to -c)
    -o OUTTYPE --outtype=OUTTYPE  the datatype to get (joining on value COLUMN) (whitespace-separated list of comma-separated tuples)
    -n --noheader                 the input data does not contain a header (must use integer indexing)
Lists:
    --list-marts     show all available marts
    --list-datasets  show all available datasets for MART
    --list-kinds     show all kinds of data available for MART and DATASET
    --list-examples  show examples of all kinds of data for MART and DATASET
    --list-columns   show column numbers next to data to help write queries
Web:
    --website  visit github.com/endrebak/biomartian for more examples and docs
    --issues   visit the issues page for biomartian to ask questions, make suggestions or report bugs
"""


# Formatting:
#     --stackcol  if multiple stackcol rows per indexcol, merge them into comma-separated list indexcol:stackcol

from docopt import docopt



# from add_columns.add_columns import add_columns
# from read_indata.read_indata import read_indata

# from config import logging_settings
# from config.cache_settings import memory


# logging_settings.set_up_logging(level=logging.DEBUG)

if __name__ == "__main__":


    args = docopt(__doc__, help=True)

    # if args["--website"]:
        # webbrowser.open_new_tab("http://github.com/endrebak/biomartian")
    # if args["--issues"]:
        # webbrowser.open_new_tab("http://github.com/endrebak/biomartian/issues")
    # else:
        # delay loading so that help message screen shown instantaneously
        # from biomart.query_bm import get_bm

    from args.validate_args import validate_args
    from args.parse_args import parse_args

    validate_args(args)
    args = parse_args(args)
    print(args)



    # validate_args(args)

    # website, issues = args["--website"]

    # intype, outtype, dataset, mart = extract_args("get_bm", args)
    # get_bm(intype, outtype, dataset, mart)

    #

    # df.to_csv(sys.stdout, index=False, sep="\t")
    # for intype, outtype, timestamp in timestamps:
    #     logging.info('Map between "{}" and "{}" from dataset "{}" downloaded' \
    #                 ' from biomart {} at {}.' \
    #                 .format(intype, outtype, dataset, mart, timestamp))
