from merge_bm_and_infile.add_col import attach_column

def attach_all_columns(in_df, column_df_map):

    # only sorting to get consistent output value for unit-tests
    for merge_on, intype in sorted(column_df_map):
        data_df = column_df_map[merge_on, intype]
        in_df = attach_column(in_df, data_df, merge_on, intype)

    return in_df
