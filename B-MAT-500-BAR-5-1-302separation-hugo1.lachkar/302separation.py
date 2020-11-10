#!/usr/bin/env python

import sys
from loops import *


def main(args):
    try:
        if (len(args) == 2):
            list_graph(args[0], int(args[1]))
        elif (len(args) == 3):
            only_connection(args[0], args[1], args[2])
        else:
            sys.exit(84)
    except:
        sys.exit(84)

contents = {}
main(sys.argv[1:])
