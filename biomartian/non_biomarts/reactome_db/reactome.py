import pandas as pd


def get_definition(pathways="non_biomart/reactome_db/reactome/data/"
                   "ReactomePathways.txt.gz"):

    # Due to bug https://support.bioconductor.org/p/62685/ using text files
    # instead of reactome.db in R

    pathways_df = pd.read_table(pathways, header=None, names=["reactome",
                                                              "reactome_definition"],
                                compression="infer", usecols=[0, 1])

    return pathways_df
