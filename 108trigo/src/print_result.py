#!/usr/bin/env python3

def print_result(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%.2f" %matrix[i][j], end='')
            if (j < len(matrix[i]) - 1):
                print('\t', end='')
        print('')