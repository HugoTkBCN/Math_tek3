#!/usr/bin/env python
import sys
from connections import *

def only_connection(file_name, p1, p2):
    contents = read_file(file_name)
    print("Degree of separation between ", p1," and ", p2, ": ", get_connect(contents, p1, p2), sep="")

def prebuild_graph(n, graphique_relation):
    graph = [[sys.maxsize] * n for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if (graphique_relation[i][j] > 0):
                graph[i][j] = 1
        graph[i][i] = 0
    return (graph)

def build_graph(graphique_relation):
    n = len(graphique_relation)
    graph = prebuild_graph(n, graphique_relation)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return (graph)

def init_graph(names, contents):
    graphique_relation = []
    for name in names:
        print(name)
        graphique_relation.append([is_friend(contents, name, i) for i in names])
    print()
    return (graphique_relation)

def print_fist_graph(names, contents, n):
    for name in names:
        index = 0
        for i in names:
            print(is_friend(contents, name, i), end="")
            index += 1
            if (index != n):
                print(end=" ")
        print()

def print_second_graph(graph, max_size, n):
    for i in range(0, len(graph)):
        index = 0
        for y in graph[i]:
            if (y <= max_size):
                print(y, end="")
            else:
                print("0", end="")
            index += 1
            if (index != n):
                print(end=" ")
        print()

def list_graph(file_name, max_size):
    if (max_size < 0):
        sys.exit(84)
    contents = read_file(file_name)
    names = sorted(contents.keys())
    graphique_relation = init_graph(names, contents)
    graph = build_graph(graphique_relation)
    n = len(names)
    print_fist_graph(names, contents, n)
    print()
    print_second_graph(graph, max_size, n)