def attach_column(in_df, map_df, merge_on, intype):

    merge_on = get_column_to_merge_on(in_df.columns, merge_on)

    relevant_maps = map_df[map_df[intype].isin(in_df[merge_on])].dropna()

    in_df = in_df.merge(relevant_maps, left_on=merge_on, right_on=intype, how="outer")
    in_df = in_df.drop(intype, axis=1).dropna().drop_duplicates()

    return in_df

def get_column_to_merge_on(in_df_columns, merge_on_int_or_string):
    """Users can use both an int or a name to choose columns.

    This method takes care of the conversions."""

    try:
        merge_on = list(in_df_columns)[merge_on_int_or_string]
    except TypeError: # merge on was already a string
        merge_on = merge_on_int_or_string

    return merge_on
