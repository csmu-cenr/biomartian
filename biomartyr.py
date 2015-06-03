# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
import pyper as pr
import pandas as pd
from joblib import Memory
import logging
import sys
from os.path import basename, join as path_join
from subprocess import call

import numpy as np

memory = Memory(cachedir="./temp/", verbose=0)

logging.basicConfig(level=logging.DEBUG, format='%(message)s (Module: %(module)s, Time: %(asctime)s)',
                    datefmt='%a, %d %b %Y %H:%M:%S', stream=sys.stderr)

def set_up_mart(r_session, dataset):

    logging.info("Loading biomaRt.")
    r_session("library(biomaRt)")

    get_mart_command = 'mart <- useMart("ensembl", dataset="{}")'.format(dataset)
    r_session(get_mart_command)

def convert_gene_name_to_entrez(r_session, gene_names_series):

    converted_files = {}
    for filename, gene_names in gene_names_series.items():

        logging.info("Converting {} gene names in file {} to entrez gene ID".format(len(gene_names), filename))

        r_session.assign("genes", gene_names)
        r_session("genes <- unlist(genes)")
        r_session.get("genes")
        r_session("gene_map_entrez <- getBM(attributes=c('external_gene_name', 'refseq_mrna'), filters = 'refseq_mrna', values = genes, mart = mart)")

        gene_name_map = r_session("gene_map_entrez")

        gene_name_map = pd.read_table(io.StringIO(gene_name_map),
                                      skiprows=[0, 1], usecols=[1,2],
                                      index_col=0, names=["Gene", "Entrez"],
                                      header=None, sep="\s+", squeeze=True).dropna()

        converted_files[filename] = gene_name_map

    return converted_files


def get_genes(input_files):

    genes = {}
    for gene_file in input_files:
        with open(gene_file) as gene_file_handle:
            genes_in_file = [line.strip() for line in gene_file_handle.readlines()]
            genes[gene_file] = pd.Series(genes_in_file)

    return genes
    # assert len(genes) != 0, "No genes found in file (s)"
    # rowlength_splitting_on_whitespace = [len(gene.split()) for gene in genes]
    # assert len(set(rowlength_splitting_on_whitespace)) == 1, "Some rows have multiple columns (or gene names with whitespace)."
    # assert rowlength_splitting_on_whitespace[0] == 1, "Rows have more than one column (or gene names contain whitespace)"



def main(outfolder, input_files):

    logging.info("Output folder: {}".format(outfolder))
    call("mkdir -p {}".format(outfolder), shell=True)

    basenames_only = [basename(infile) for infile in input_files]
    assert len(basenames_only) == len(set(basenames_only)), "Some files share the same name! Exiting..."

    logging.info("Input files: {}".format(", ".join(input_files)))
    gene_series = get_genes(input_files)

    r_session = pr.R(use_pandas=True)

    set_up_mart(r_session, "rnorvegicus_gene_ensembl")

    converted_files = convert_gene_name_to_entrez(r_session, gene_series)

    for infile, converted_genes in converted_files.items():

        outpath = path_join(outfolder, basename(infile))
        converted_genes.to_csv(outpath, index=True, sep="\t")


if __name__ == '__main__':

    outfolder = sys.argv[1]
    input_files = sys.argv[2:]

    main(outfolder, input_files)

 #j def
#     gene.data <- getBM(attributes=c('hgnc_symbol', 'ensembl_transcript_id', 'go_id'),
#                        filters = 'go_id', values = 'GO:0007507', mart = mart)
