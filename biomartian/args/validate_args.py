def validate_args(args):

    validate_same_number_of_args(args)
    validate_outindexes_must_be_same_length_if_used(args)


def validate_same_number_of_args(args):

    columns, intypes, outtypes = args["--column"], args["--intype"], args["--outtype"]
    if not len(columns) == len(intypes) == len(outtypes):

        msg = "Number of args for --column, --intype and --outtype must be equal," \
              " but they are not: --column {} {} \n--intype {} {} \n--outtype {} {}" \
                  .format(columns, len(columns), intypes, len(intypes), \
                          outtypes, len(outtypes))
        raise ValueError(msg)

def validate_outindexes_must_be_same_length_if_used(args):

    columns = args["--column"]
    outindexes = args["--outindex"]

    if len(outindexes) and len(outindexes) != len(columns):

        msg = "If there are any outindex arguments, they must have" \
              " the same number of elements as arguments --column, --intype" \
                  " and --outtype."

        raise ValueError(msg)
