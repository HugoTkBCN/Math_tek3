#!/usr/bin/env python3

def get_connection(file, commands):
    to_print = []
    for command in commands:
        if (command == file or command.is_linked(file)):
            to_print.append(command.get_connection())
    for element in sorted(to_print):
        print(element)

def find_connection(i, array, files, commands, find):
    for j, _ in enumerate(files):
        if (array[j][i] == 1):
            get_connection(files[j if find else i], commands)
            find_connection(j, array, files, commands, True)
            break

def print_connections(array, file, files, commands):
    i = files.index(file)
    find_connection(i, array, files, commands, False)