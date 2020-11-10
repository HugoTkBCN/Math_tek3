#!/usr/bin/env python3

def print_matrice(array):
    for line in array:
        print(str(line).replace(",", ""))
    print()

def transpose_array(array):
    new_array = [[] for _ in array]
    for i in range (0, len(array)):
        for y in range (0, len(array)):
            new_array[y].append(array[i][y])
    return (new_array)

def get_array(commands, files):
    array = []
    for file in files:
        if (file not in commands):
            array.append([0 for _ in files])
        else:
            command = commands[commands.index(file)]
            array.append([command.is_linked(tmp) for tmp in files])
    return (array)


def find_connection(i, array, files, find):
    for j, _ in enumerate(files):
        if (array[j][i] == 1):
            print(" -> " + files[j], end="", sep="") if (find) else print(files[i], " -> ", files[j], end="", sep="")
            find_connection(j, array, files, True)
            if (find):
                break
            else:
                print()

def print_all(array, commands, files):
    print_matrice(transpose_array(array))
    for i, _ in enumerate(files):
        find_connection(i, array, files, False)
