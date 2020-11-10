#!/usr/bin/env python

import sys

def fill_content(first, second, contents):
    if (first in contents):
        contents[first].append(second)
    else:
        contents[first] = [second]
    if (second in contents):
        contents[second].append(first)
    else:
        contents[second] = [first]
    return (contents)

def read_file(file_name):
    f = open(file_name, "r")
    contents = {}
    for line in f.readlines():
        try:
            first, second = line.strip().split(" is friends with ")
        except:
            continue
        contents = fill_content(first, second, contents)
    f.close()
    return (contents)

def is_friend(contents, p1, p2):
    return ((int)(p2 in contents[p1]))

def get_small_connection(contents, p1 , p2):
    for friend in contents[p1]:
        if (friend == p2):
            return (1)
    return (0)

def get_large_connection(contents, p1, p2, visited, max_size):
    nb = 1
    minimum = sys.maxsize
    assigned = False
    for friend in contents[p1]:
        if (friend not in visited):
            tmp_connections = get_connect(contents, friend, p2, visited + [p1], max_size)
            if (0 < tmp_connections < minimum):
                if (tmp_connections == 1):
                    return (nb + tmp_connections)
                minimum = tmp_connections
                assigned = True
    if assigned:
        return (nb + minimum)
    return (nb - 2)

def get_connect(contents, p1, p2, visited=[], max_size=-1):
    if (p1 not in contents) or p2 not in contents or 0 <= max_size <= len(visited):
        return (-1)
    if (p1 == p2):
        return (0)
    if (get_small_connection(contents, p1, p2) != 0):
        return (1)
    return (get_large_connection(contents, p1 ,p2, visited, max_size))