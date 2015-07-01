from widediaper import R


def set_up_mart(mart, dataset=None, outstream=False):

    r = R(outstream)

    r.load_library("biomaRt")

    if dataset:
        get_mart_command = ('mart <- useMart("{mart}", dataset = "{dataset}")'
                            .format(**vars()))
    else:
        get_mart_command = 'mart <- useMart("{mart}")'.format(mart=mart)

    r(get_mart_command)

    return r
