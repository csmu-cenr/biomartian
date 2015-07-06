import sys


def attach_column(in_df, map_df, merge_on, intype):

    in_df_cols = list(in_df.columns)
    merge_on = get_column_to_merge_on(in_df_cols, merge_on)
    relevant_maps = map_df[map_df[intype].isin(in_df[merge_on])].dropna()

    nb_columns_pre_merge = len(in_df.columns)

    # adding integer index as regular column to preserve sort order after merge
    in_df = in_df.reset_index()
    in_df = in_df.merge(relevant_maps, left_on=merge_on, right_on=intype,
                                      how="outer", sort=False)
    in_df = in_df.sort("index")

    # dropping the index we created
    in_df = in_df.drop(list(in_df.columns)[0], axis=1)

    # TODO: should we really drop NA? Should at least be an option, right?
    in_df = in_df.dropna().drop_duplicates()

    if nb_columns_pre_merge + 2 == len(in_df.columns):
        # if two columns were added in the merge, the df did not contain a column
        # labeled INTYPE to begin with, so we may drop it.
        in_df = in_df.drop(intype, axis=1)

    return in_df


def get_column_to_merge_on(in_df_columns, merge_on_int_or_string):
    """Users can use both an int or a name to choose columns.

    This method takes care of the conversions."""

    try:
        merge_on = in_df_columns[int(merge_on_int_or_string)]
    except ValueError: # merge on was already a string
        merge_on = merge_on_int_or_string

    return merge_on
