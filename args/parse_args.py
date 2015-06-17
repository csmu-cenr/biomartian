def parse_args(args):

    if args["--intype"] and args["--outtype"]:
        args["--outtype"] = [s.split(",") for s in args["--outtype"].split()]
        args["--intype"] = args["--intype"].split(",")

    args["--column"] = args["--column"].split(",")

    return args
