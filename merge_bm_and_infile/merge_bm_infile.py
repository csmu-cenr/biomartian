from collections import defaultdict

from merge_bm_and_infile.add_col import attach_column

def attach_all_columns(in_df, column_df_map):

    # only sorting to get consistent output value for unit-tests
    for merge_on, intype in sorted(column_df_map):
        data_dfs = column_df_map[merge_on, intype]
        for data_df in data_dfs:
            in_df = attach_column(in_df, data_df, merge_on, intype)

    return in_df

def convert_in_out_map_to_merge_in_map(intype_outtype_df_map, merge_cols, intypes, outtypes):

    merge_col_to_intype_map = defaultdict(list)
    for merge_col, intype, outtype_list in zip(merge_cols, intypes, outtypes):

        for outtype in outtype_list:
            dfs = intype_outtype_df_map[intype, outtype]
            for df in dfs:
                merge_col_to_intype_map[merge_col, intype].append(df)

    return merge_col_to_intype_map
