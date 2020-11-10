#!/usr/bin/env python3

from command import *
import sys

def print_help():
    print("USAGE")
    print("    ./303make makefile [file]")
    print("DESCRIPTION")
    print("    makefile    name of the makefile")
    print("    file        name of a recently modified file")

def transpose_files(files):
    result = []
    for list_files in files:
        for file in list_files:
            if (file not in result):
                result.append(file)
    return (result)

def get_line(line):
    to_return = []
    for c in line.replace(":", " ").split():
        to_return.append(c.strip())
    return (to_return)

def get_file(file_path): ####
    commands = []
    files = []
    lines = open(file_path, "r").readlines()
    if (not lines):
        sys.exit(84)
    for line in lines:
        line = line.strip()
        if (not line):
            continue
        if (":" in line):
            commands.append(Command(line))
            files.append(get_line(line))
        else:
            commands[-1].set_connection(line)
    files = transpose_files(files)
    files.sort()
    return (commands, files)