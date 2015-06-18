import pandas as pd
import os.path.join as path_join
from r.r import CheckedRSession

import logging

from joblib import Memory

from utils.helper_functions import init_worker
from config.cache_settings import default_cache_path

MEMORY = Memory(cachedir="./")


def get_annotations_for_go(cache_path=default_cache_path):

    r_session = CheckedRSession()

    r_session.call("library(GO.db)")
    r_session.call("df <- as.data.frame(GOTERM)")
    r_session.call("subset_df <- subset(df, select=c('go_id', 'Term'))")

    outfile = path_join(default_cache_path, "other_data/") + "go_annotations.txt"

    write_command = """

    write.table(subset_df, '{}', sep='\t', row.names=F)

    """.format(outfile)

    r_session.call(write_command)

    map_df = pd.read_table(outfile, header=0, dtype=str)

    return map_df


def get_annotations_for_reactome(terms, dataset, pathways="data/ReactomePathways.txt.gz"):

    # Due to bug https://support.bioconductor.org/p/62685/ using text files instead

    ensembl_to_reactome = {"rnorvegicus_gene_ensembl": "Rattus norvegicus",
                           "hsapiens_gene_ensembl": "Homo sapiens",
                           "mmusculus_gene_ensembl": "Mus musculus"}

    pathways_df = pd.read_table(pathways, header=None, names=["term", "go_annotation", "Species"], compression="infer")

    species = ensembl_to_reactome[dataset]
    pathways_df_correct_species = pathways_df[pathways_df["Species"] == species]

    df = pd.DataFrame(pd.concat([pathways_df_correct_species["term"],
                                 pathways_df_correct_species["go_annotation"]], axis=1))

    df = df.drop_duplicates()
    df = df[df["term"].isin(terms)]

    assert len(df) == len(terms), \
        "Output annotation df {} does not have the same length"\
        "as list of input terms {}".format(len(df), len(terms))
    df.columns = ["term", "go_annotation"]

    return df

    # annotations = pd.Series(annotations, index=terms.index)
    # term_to_annotation = pd.DataFrame(pd.concat([terms, annotations], axis=1))
