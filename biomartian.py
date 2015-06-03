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

from __future__ import print_function

import pyper as pr
import pandas as pd
import logging
import sys
from sys import stdout

# ugly hack to support python2 and 3
try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO


def set_up_mart(r_session, dataset):

    r_session("library(biomaRt)")

    get_mart_command = 'mart <- useMart("ensembl", dataset="{}")'.format(dataset)
    r_session(get_mart_command)


def convert_genes(r_session, genes, input_type, output_type, gene_column):

    r_session.assign("genes", genes)
    r_session("converted_genes <- getBM(attributes=c('{input_type}', '{output_type}'), filters = '{input_type}', values = genes, mart = mart)".format(input_type=input_type,
                                                                                                                                                      output_type=output_type))

    gene_name_map = r_session("converted_genes")

    gene_name_map = pd.read_table(StringIO(gene_name_map),
                                  skiprows=[0, 1], usecols=[1,2],
                                  names=[gene_column, output_type],
                                  header=None, sep="\s+").dropna(how="any")

    return gene_name_map


def main(gene_column, input_type, output_type, species, input_file):

    logging.info("Reading input table from file: {}".format(input_file))
    df = pd.read_table(input_file)
    genes = df[gene_column]

    r_session = pr.R(use_pandas=True)
    logging.info("Loading biomaRt for species: {}".format(species))
    set_up_mart(r_session, species)

    logging.info("Converting {} gene names in file {} to {}".format(len(genes), input_file, output_type))
    converted_genes = convert_genes(r_session, genes, input_type, output_type, gene_column)
    converted_genes.to_csv("testing")


    logging.info("Creating new dataframe with additional gene names.")
    final_df = df.merge(converted_genes, on=gene_column)

    final_df.to_csv(stdout, sep="\t", index=False, na_rep="NA")


if __name__ == '__main__':

    gene_column = sys.argv[1]
    input_type = sys.argv[2]
    output_type = sys.argv[3]
    species = sys.argv[4]
    input_file = sys.argv[5]
    should_log = sys.argv[6:7]


    if should_log == ["logging"]:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s (Time: %(asctime)s)',
                            datefmt='%a, %d %b %Y %H:%M:%S', stream=sys.stderr)


    main(gene_column, input_type, output_type, species, input_file)
