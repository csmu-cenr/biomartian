def validate_args(args):

    columns, intypes, outtypes = args["--column"], args["--intype"], args["--outtype"]
    validate_list_lengths(columns, intypes, outtypes)

def validate_list_lengths(columns, intypes, outtypes):
    if not len(columns) == len(intypes) == len(outtypes):

        msg = "Number of args for --column, --intype and --outtype must be equal," \
              " but they are not: --column {} {} \n--intype {} {} \n--outtype {} {}" \
                  .format(columns, len(columns), intypes, len(intypes), \
                          outtypes, len(outtypes))
        raise ValueError(msg)
