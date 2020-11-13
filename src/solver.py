# -*- coding: utf-8 -*-

import sys
from knapsack_solver import *

def help():
    print("Este programa..")

def main(args):
    if "-h" in args:
        help()
        exit(0)

    if len(args) != 4:
        print("Uso: python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO")
        exit(1)

    knapsack = False

    if args[1] == 1:
        knapsack = True

    brute_force = False

    if args[2] == 1:
        brute_force = True

    file_path = args[3]
    input = input(file_path)

    if(knapsack):
        if(brute_force):
            knapsack_brute_force_solver(input)
        else:
            knapsack_dynamic_solver(input)
    #TODO
    '''else:
        if (brute_force):

        else:'''


if __name__ == '__main__':
    main(sys.argv)