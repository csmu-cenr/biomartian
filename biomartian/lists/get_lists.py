import re
from os import walk
from os.path import join as path_join

import pandas as pd

from widediaper import R
from biomartian.r.r import set_up_mart
# from biomartian.get_mappings.get_data import get_non_bm

from py.path import local

def get_non_bm_attributes(dataset_file):

    contents = local(dataset_file).read()

    attribute_re = re.compile(r"def\sget_(\w+)\(\)", flags=re.MULTILINE)

    attributes = [match.groups()[0] for match in attribute_re.finditer(contents)]

    return attributes


def get_non_bm(external_marts_folder="biomartian/non_biomarts"):

    rowdicts = []
    marts = walk(external_marts_folder).next()[1]

    for mart in marts:
        mart_path = path_join(external_marts_folder, mart)

        dataset_files = walk(mart_path).next()[2]
        dataset_files = [f for f in dataset_files if f != "__init__.py"]

        for dataset_file in dataset_files:
            dataset = dataset_file.replace(".py", "")
            dataset_file = path_join(mart_path, dataset_file)

            attributes = get_non_bm_attributes(dataset_file)

            for attribute in attributes:
                rowdict = {"mart": mart, "dataset": dataset,
                           "attribute": attribute}
                rowdicts.append(rowdict)

    external_marts_df = pd.DataFrame.from_dict(rowdicts)


    return external_marts_df[["mart", "dataset", "attribute"]]

def get_marts():

    print("in get marts")
    non_biomarts = get_non_bm()
    # biomarts = get_bm_marts()

    return non_biomarts

def get_bm_marts():

    r = R()
    r.load_library("biomaRt")
    r("marts = listMarts()")
    return r.get("marts")

def get_bm_datasets(mart):

    r = set_up_mart(mart)
    r("datasets = listDatasets(mart)")
    return r.get("datasets")

def get_bm_attributes(mart, dataset):

    r = set_up_mart(mart, dataset)
    r("attributes = listAttributes(mart)")
    return r.get("attributes")
