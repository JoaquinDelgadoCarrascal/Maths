#!/usr/bin/env python3

from sys import argv
from src.taylor_expansions.taylor_functions import *

def taylor_expansions():
    if argv[1] == 'EXP':
        taylor_exp()
    elif argv[1] == 'COS':
        taylor_cos()
    elif argv[1] == 'SIN':
        taylor_sin()
    elif argv[1] == 'COSH':
        taylor_cosh()
    elif argv[1] == 'SINH':
        taylor_sinh()
    else:
        print ("Error: wrong function name, try -h to see the USAGE")
        exit(84)