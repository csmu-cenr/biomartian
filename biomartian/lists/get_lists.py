import re
from os import walk
from os.path import join as path_join

import pandas as pd

from biomartian.r.r import set_up_mart

from py.path import local

def get_non_bm_attributes(dataset_file):

    contents = local(dataset_file).read()

    attribute_re = re.compile(r"def\sget_(\w+)\(\)", flags=re.MULTILINE)

    attributes = [match.groups()[0] for match in attribute_re.finditer(contents)]

    return attributes


def get_non_bm(external_marts_folder="biomartian/non_biomarts"):

    rowdicts = []
    for path, _, files in walk(external_marts_folder):

        if path.count("/") != 3:
            continue

        mart = path.split("/")[-1]

        for dataset_file in [f for f in files if f != "__init__.py"]:
            dataset = dataset_file.replace(".py", "")
            dataset_file = path_join(path, dataset_file)

            attributes = get_non_bm_attributes(dataset_file)

            for attribute in attributes:
                rowdict = {"mart": mart, "dataset": dataset,
                           "attribute": attribute}
                rowdicts.append(rowdict)

    external_marts_df = pd.DataFrame.from_dict(rowdicts)

    return external_marts_df[["mart", "dataset", "attribute"]]
