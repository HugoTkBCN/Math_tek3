#!/usr/bin/env python3

import sys
from utils import *
from connections import *
from matrice import *
from command import *

def run(args):
    commands, files = get_file(args[0])
    array = get_array(commands, files)
    if (len(args) == 1):
        print_all(array, commands, files)
    else:
        print_connections(array, args[1], files, commands)

def main(args):
    if (len(args) == 1 and args[0] == "-h"):
        print_help()
    elif (len(args) == 1 or len(args) == 2):
        run(args)
    else:
        sys.exit(84)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except:
        sys.exit(84)