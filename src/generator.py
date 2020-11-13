#python3 generator.py W N minPeso maxPeso minBeneficio maxBeneficio
#minCantidad maxCantidad

# -*- coding: utf-8 -*-

import sys
from knapsack_generator import knapsack_generator

def help():
    print("Este programa..")

def main(args):
    '''if len(args) != 4:
        print("Uso: ")

    knapsack = False

    if args[1] == 1:
        knapsack = True

    #file_path = args[2]'''

    weight = args[1]
    quantity = int(args[2])
    min_weight = int(args[3])
    max_weight = int(args[4])
    min_value = int(args[5])
    max_value = int(args[6])
    min_quantity = int(args[7])
    max_quantity = int(args[8])

    knapsack_generator(weight, quantity, min_weight, max_weight, min_value, max_value, min_quantity, max_quantity)

if __name__ == '__main__':
    main(sys.argv)