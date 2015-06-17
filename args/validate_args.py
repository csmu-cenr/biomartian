def validate_args(args):


    if args["--intype"] and args["--outtype"]:
        validate_column_list_lengths(args["--column"], args["--intype"], args["--outtype"])

def validate_column_list_lengths(incols, intypes, outtypes):

    incols_len = len(incols.split(","))
    intypes_len = len(intypes.split(","))
    outtypes_len = len(outtypes.split(" "))

    if incols_len != intypes_len:
        raise ValueError("Number of input columns and input types must be equal" \
                         ", but they are not: columns: {} ({}) {} ({})." \
                         .format(incols, incols_len, intypes, intypes_len))

    if outtypes_len < intypes_len:
        raise ValueError("\nThere must be at least as many (space-separated) outtypes" \
                         " as comma-separated intypes:\n" \
                         "outtype args: {} ({}),\nintype args: {} ({})." \
                         .format(outtypes, outtypes_len, intypes, intypes_len))
