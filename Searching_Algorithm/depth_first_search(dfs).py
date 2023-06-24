# -*- coding: utf-8 -*-
"""Depth_First_Search(DFS).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

import inspect


def search(graph, start, path=[]):
    """
    depth first search algorithm

    :param graph:
    :param start:
    :param path:
    :return:
    """
    # check if graph is empty or start vertex is none
    if start not in graph or graph[start] is None or graph[start] == []:
        return path

    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = search(graph, edge, path)
    return path


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "O(V + E) where V = Number of vertices and E = Number of Edges"


def get_code():
    """
    easily retrieve the source code
    of the function

    :return: source code
    """
    return inspect.getsource(search)