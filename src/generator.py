#python3 generator.py W N minPeso maxPeso minBeneficio maxBeneficio
#minCantidad maxCantidad

# -*- coding: utf-8 -*-

import sys
from knapsack_generator import knapsack_generator
from sequences_generator import sequences_generator


def help():
    print("Este programa..")

def main(args):
    knapsack = False

    if args[1] == 1:
        knapsack = True

    file_path = args[2]


    if knapsack:
        if len(args) != 11:
            print("Uso: ")

        weight = args[3]
        quantity = int(args[4])
        min_weight = int(args[5])
        max_weight = int(args[6])
        min_value = int(args[7])
        max_value = int(args[8])
        min_quantity = int(args[9])
        max_quantity = int(args[10])

        knapsack_generator(file_path, weight, quantity, min_weight, max_weight, min_value, max_value, min_quantity, max_quantity)
    else:
        if len(args) != 5:
            print("Uso: ")

        length1 = int(args[3])
        length2 = int(args[3])

        sequences_generator(length1, length2)


if __name__ == '__main__':
    main(sys.argv)