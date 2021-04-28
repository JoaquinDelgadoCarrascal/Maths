#!/usr/bin/env python3

from sys import argv
from math import *

def is_quadratic():
    square_root = sqrt(len(argv) - 2)
    tmp = int(round(square_root))

    if square_root == tmp:
        return True
    return False