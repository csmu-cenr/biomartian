
import pandas as pd
import logging
import sys

def read_indata(infile, noheader):

    infile = sys.stdin if infile == "-" else infile

    if noheader:
        df = pd.read_table(infile, header=None, dtype=str)
    else:
        df = pd.read_table(infile, header=0, dtype=str)

        # if the index is a data column
        if not all(df.index == range(len(df))):
            logging.debug("Resetting index on\n" + str(df.head()))
            df = df.reset_index()

    return df