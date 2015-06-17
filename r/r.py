import logging

from pyparsing import nestedExpr, quotedString

import pyper as pr


class CheckedRSession():

    def __init__(self, debug=False):
        self.R = pr.R(use_pandas=True)
        self.debug = debug

    def call(self, command):
        check_r_command_string(command)

        if self.debug:
            logging.debug("Command used:" + command)

        return_value = self.R(command)
        logging.debug("Return value: " + str(return_value))

        return return_value


def set_up_mart(mart, dataset=None):

    r = CheckedRSession(debug=True)

    r.call("library(biomaRt)")

    if dataset:
        get_mart_command = 'mart <- useMart("{}", dataset = "{}")'.format(mart, dataset)
    else:
        get_mart_command = 'mart <- useMart("{}")'.format(mart)

    r.call("options(max.print=1000000)")

    r.call(get_mart_command)

    return r


class UnmatchedRCommandStringException(Exception):
    pass


def check_r_command_string(command_string):

    paired_symbols = "".join([c for c in command_string if c in
                              ["'", '"', '(', ')']])
    paired_exprs = nestedExpr('(',')') | quotedString

    unmatched = paired_exprs.suppress().transformString(paired_symbols)
    if unmatched:
        e_s = "Unmatched paranthesis or quote in {}. Unable to continue." \
            .format(command_string)
        raise ValueError(e_s)
