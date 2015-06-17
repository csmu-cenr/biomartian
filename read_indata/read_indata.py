
import pandas as pd
import logging

def read_indata(infile, header):

    if header:
        df = pd.read_table(infile, header=0, dtype=str, sep="\s+")

        # if the index is a data column
        if not all(df.index == range(len(df))):
            logging.debug("Resetting index on\n" + str(df.head()))
            df = df.reset_index()
    else:
        df = pd.read_table(infile, header=None, dtype=str, sep="\s+")

    return df
