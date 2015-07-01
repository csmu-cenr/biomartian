
import pandas as pd
from os.path import join as path_join

from subprocess import call

from biomartian.config.cache_settings import default_cache_path, memory

from widediaper import R

def get_other(intype, outtype, dataset):

    if dataset == "go_annotation":
        return get_go(intype, outtype)
    elif dataset == "reactome_annotation":
        return get_reactome()


def get_go(intype, outtype, cache_path=default_cache_path):

    # call("mkdir -p {}/human_readable/".format(cache_path), shell=True)
    r = R()

    r.load_library("GO.db")
    r("df <- as.data.frame(GOTERM)")
    r("subset_df <- subset(df, select=c('{}', '{}'))".format(intype, outtype))

    map_df = r.get("subset_df")

    return map_df


def get_reactome(pathways="data/ReactomePathways.txt.gz"):

    # Due to bug https://support.bioconductor.org/p/62685/ using text files instead

    pathways_df = pd.read_table(pathways, header=None, names=["reactome",
                                                              "reactome_annotation"],
                                compression="infer", usecols=[0, 1])

    return pathways_df
