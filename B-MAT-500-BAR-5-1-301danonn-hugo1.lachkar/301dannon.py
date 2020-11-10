#!/usr/bin/python3

import sys
from utils import check_arg, get_values, print_res
from bubble import bubble
from selection import selection
from insertion import insertion
from merge import merge
from quicksort import quicksort

def main(args):
    numbers = get_values(args[0])
    if (len(numbers) <= 0):
        sys.exit(84)
    print(len(numbers), " element", sep="", end="")
    print("s" if len(numbers) > 1 else "")
    selection(numbers[::])
    insertion(numbers[::])
    bubble(numbers[::])
    print_res("Quicksort:", 0 if (len(numbers) <= 1) else quicksort(numbers[::])[1])
    print_res("Merge sort:", merge(numbers[::])[1])

try:
    check_arg(sys.argv)
    main(sys.argv[1:])
except:
    sys.exit(84)