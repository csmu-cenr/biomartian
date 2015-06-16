import sys
import logging

import pandas as pd
import pyper as pr


from add_columns.add_columns import add_columns

from config import logging_settings
from config.cache_settings import memory


# have option --noheader
# r tables without name of first column is read with index column as index
# check for this with all(df.index == range(len(df)))
# if this is true run reset_index()

# def add_columns(df, additions):

# logging_settings.set_up_logging(level=logging.DEBUG)






if __name__ == "__main__":

    # intype, outtype = "external_gene_name", "entrezgene"

    dataset, mart = "rnorvegicus_gene_ensembl", "ensembl"
    # timestamp, df = get_timestamped_data(intype, outtype, dataset, mart)

    infile = "examples/test_file.txt"
    df = pd.read_table(infile)
    df = df.reset_index()
    # print(df)
    # raise

    dataset = "rnorvegicus_gene_ensembl"

    additions_to_make = {"external_gene_name": {"out_types": ["go_id", "entrezgene"],
                                                "non_long": ["go_id"],
                                                "insert_positions": [0, 5],
                                                "merge_on": 0}}


    df, timestamps = add_columns(df, dataset, mart, additions_to_make)
    df.to_csv(sys.stdout, index=False, sep="\t")
    for intype, outtype, timestamp in timestamps:
        logging.info('Map between "{}" and "{}" from dataset "{}" downloaded' \
                    ' from biomart {} at {}.' \
                    .format(intype, outtype, dataset, mart, timestamp))
