
def get_final_outcolumn_order(outindexes, header, merge_on_cols):

    # FIXME: the code below hinges on the fact that new header in same order
    # as outindexes and merge_on_cols. Bad practice to have implicit structure
    # like this...

    nb_new_cols = len(merge_on_cols) or len(outindexes)
    old_header, new_header = header[:-nb_new_cols], header[-nb_new_cols:]

    if outindexes:
        outindexes = _correct_outpositions(outindexes)
    else:
        outindexes = _find_outindexes(header, merge_on_cols)
        outindexes = _correct_outpositions(outindexes)
        outindexes = [i + 1 for i in outindexes]


    for i, out_ix in enumerate(outindexes):
        old_header.insert(out_ix, new_header[i])

    return old_header


def _correct_outpositions(outindexes):

    """if a and b should be inserted in position 0 and 5 in the original array
       bs index must be increased by 1 after a is inserted and so on."""

    proper_outindexes = [i + c for i, c in enumerate(outindexes)]

    return proper_outindexes


def _find_outindexes(header, merge_on_cols):

    outindexes = []
    for merge_col in merge_on_cols:
        for i, header_col in enumerate(header):
            if merge_col == header_col:
                outindexes.append(i)

    return outindexes
