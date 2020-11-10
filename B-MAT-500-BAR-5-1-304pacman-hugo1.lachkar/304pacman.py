#!/usr/bin/env python3
import sys
from utils import checkArgs, printHelp
from buildArray import run

def main(ac, av):
    if (ac == 4):
        contentFile, c1, c2 = checkArgs(av)
        run(contentFile, c1, c2)
    elif (ac == 2):
        if (av[1] == "-h"):
            printHelp()
        else:
            sys.exit(84)
    else:
        sys.exit(84)
    sys.exit(0)

main(len(sys.argv), sys.argv)