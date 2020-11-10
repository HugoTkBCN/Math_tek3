import sys

def check_arg(args):
    if (len(args) != 2):
        sys.exit(84)
    elif (args[1] == "-h"):
        print("USAGE\n    ./301dannon file\nDESCRIPTION\n    file    file that contains the numbers to be sorted, seperated by spaces")
        sys.exit(0)

def read_file(filename):
    f = open(filename, "r")
    content = f.read().strip().replace("\t", " ").replace('\n', " ").replace(';', " ").replace(',', " ")
    content = ' '.join(content.split(" "))
    f.close()
    return (content.split(" "))

def get_values(filename):
    numbers = []
    tmp_numbers = read_file(filename)
    for number in tmp_numbers:
        if (len(number) > 0):
                numbers.append(float(number))
    return (numbers)

def print_res(sort_type, res):
    print(sort_type, " ", res, " comparisons", sep="")