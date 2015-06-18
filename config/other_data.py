import pandas as pd

from utils.unit_test_helpers import StringIO

other_data_df_string = u"""non-biomart mart    version
                           go_annotations      from R library GO.db
                           reactome_annotations   from R library reactome.db"""

other_data_df = pd.read_table(StringIO(other_data_df_string), sep=r"\s\s+", header=0, index_col=None)
