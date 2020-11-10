#!/usr/bin/env python3

import os
import sys

def printHelp():
    print("USAGE")
    print("    ./304pacman file c1 c2")
    print("DESCRIPTION")
    print("    file    file describing the board, using the following characters:")
    print("                ‘0’ for an empty square,")
    print("                ‘1’ for a wall,")
    print("                ‘F’ for the ghost’s position,")
    print("                ‘P’ for Pacman’s position.")
    print("    c1      character to display for a wall")
    print("    c2      character to display for an empty space.")

def checkArgs(av):
    if (not os.path.isfile(av[1])):
        sys.exit(84)
    if ((len(av[2]) != 1 or len(av[3]) != 1) or av[2] == av[3]):
        sys.exit(84)
    return (open(av[1]), av[2], av[3])