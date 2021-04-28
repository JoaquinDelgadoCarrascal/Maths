#!/usr/bin/env python3

from src.create_matrices import *
from src.matrix_operations import *
from src.print_result import print_result

def taylor_exp():
    A = create_argv_matrix()
    result = create_matrix(0)

    for n in range(150):
        power_matrix = matrix_to_power(A, n)
        divided_matrix = divide_matrix_to_real_number(power_matrix, factorial(n))
        result = matrices_addition(result, divided_matrix)
    print_result(result)

def taylor_sin():
    A = create_argv_matrix()
    division = 0
    result = create_matrix(0)
    final_result = create_matrix(0)

    for n in range(50):
        division = pow(-1, n)/factorial(2 * n + 1)
        power_matrix = matrix_to_power(A, 2 * n + 1)
        result = multiply_matrix_to_real_number(power_matrix, division)
        final_result = matrices_addition(final_result, result)
    print_result(final_result)

def taylor_cos():
    A = create_argv_matrix()
    division = 0
    result = create_matrix(0)
    final_result = create_matrix(0)

    for n in range(50):
        division = pow(-1, n)/factorial(2 * n)
        power_matrix = matrix_to_power(A, 2 * n)
        result = multiply_matrix_to_real_number(power_matrix, division)
        final_result = matrices_addition(final_result, result)
    print_result(final_result)

def taylor_sinh():
    A = create_argv_matrix()
    result = create_matrix(0)

    for n in range(80):
        power_matrix = matrix_to_power(A, 2 * n + 1)
        divided_matrix = divide_matrix_to_real_number(power_matrix, factorial(2 * n + 1))
        result = matrices_addition(result, divided_matrix)
    print_result(result)

def taylor_cosh():
    A = create_argv_matrix()
    result = create_matrix(0)

    for n in range(80):
        power_matrix = matrix_to_power(A, 2 * n)
        divided_matrix = divide_matrix_to_real_number(power_matrix, factorial(2 * n))
        result = matrices_addition(result, divided_matrix)
    print_result(result)