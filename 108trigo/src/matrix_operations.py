#!/usr/bin/env python3

from src.create_matrices import *

def multiply_matrices(A, B):
    result = create_matrix(0)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrices_addition(A, B):
    result = create_matrix(0)

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

def matrix_to_power(A, n):
    result = identity_matrix(len(A))

    for i in range(n):
        result = multiply_matrices(result, A)
    return result

def divide_matrix_to_real_number(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] / n
    return matrix

def multiply_matrix_to_real_number(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * n
    return matrix