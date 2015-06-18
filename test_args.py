"""biomartian

Query biomart from the command line.
For help and examples, visit github.com/endrebak/biomartian (biomartian --website)

Usage:
    biomartian [--mart=MART] [--dataset=DATASET] --column=COLUMN... --intype=INTYPE... --outtype=OUTTYPE... [--noheader] FILE

Arguments:
    FILE  file

Options:
    -h --help                     show this message
    -m MART --mart=MART           which mart to use [default: ensembl]
    -d DATASET --dataset=DATASET  which dataset to use [default: hsapiens_gene_ensembl]
    -c COLUMN --column=COLUMN     name or number of the column to join on in FILE (comma-separated)
    -i INTYPE --intype=INTYPE     the datatype in the column to merge on (comma-separated, must have length equal to COLUMN)
    -o OUTTYPE --outtype=OUTTYPE  the datatype to get (joining on value COLUMN) (whitespace-separated list of comma-separated tuples)
    -n --noheader                 the input data does not contain a header (must use integer indexing)
"""


# Formatting:
#     --stackcol  if multiple stackcol rows per indexcol, merge them into comma-separated list indexcol:stackcol

from docopt import docopt



if __name__ == "__main__":
    args = docopt(__doc__, help=True)
    print(args)
