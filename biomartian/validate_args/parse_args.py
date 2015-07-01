"""biomartian

Query biomart from the command line. For help and examples, visit github.com/endrebak/biomartian

Usage:
    biomartian (-m MART) (-d DATASET) (-c COL) (-n NEWCOL)... FILE
    biomartian --list-marts
    biomartian -m MART --list-datasets
    biomartian [--website|--issues]


Arguments:
    FILE  file with COLUMN(s) to join mart data on

Options:
    -h          show this message
    -m MART     which mart to use [default: ensembl]
    -d DATASET  which dataset to use [default: hsapiens_gene_ensembl]
    -c COLUMN   name or number of the column to join on in inputfile (comma-separated) [default: 0]
    -n DATA     the data to get (joining on value COLUMN) (comma-separated)
Lists:
    --marts     show all available marts
    --datasets  show all available datasets for MART
    --kinds     show all kinds of data available for MART and DATASET
Web:
    --website   visit github.com/endrebak/biomartian for more examples and docs
    --issues    visit the issues page for biomartian to ask questions, make suggestions or report bugs

"""

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments, "arguments")

    # TODO:
    # biomartian -c Gene GO_id -n entrezgene,HUGO go_annotations ex/test.txt

    # biomartian -m ensembl -d rnorvegicus_gene_ensembl -c Gene -n entrezgene,HUGO -c GO_id -n go_annotations ex/toplist.txt

    # biomartian -m ensembl -d rnorvegicus_gene_ensembl -c Gene -c GO_id -n entrezgene,HUGO -n go_annotations ex/toplist.txt

    # untidy
