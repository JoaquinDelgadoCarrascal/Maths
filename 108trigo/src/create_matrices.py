#!/usr/bin/env python3

from sys import argv
from math import *

def create_matrix(val):
    matrix = []
    pos_argv = 2

    for i in range(int(sqrt(len(argv) - 2))):
        matrix.append([])
        for j in range(int(sqrt(len(argv) - 2))):
            matrix[i].append(val)
            pos_argv += 1
    return matrix

def create_argv_matrix():
    matrix = []
    pos_argv = 2

    for i in range(int(sqrt(len(argv) - 2))):
        matrix.append([])
        for j in range(int(sqrt(len(argv) - 2))):
            matrix[i].append(float(argv[pos_argv]))
            pos_argv += 1
    return matrix

def identity_matrix(size):
    identity_matrix = []
    for i in range(size):
        identity_matrix.append([])
        for j in range(size):
            if i == j:
                identity_matrix[i].append(1)
            else:
                identity_matrix[i].append(0)
    return identity_matrix