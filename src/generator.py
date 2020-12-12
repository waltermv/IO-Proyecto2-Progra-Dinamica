# -*- coding: utf-8 -*-

'''
Autor: Walter Morales Vásquez
Email: waltermvgit@gmail.com

Programa para generar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.
Se recibirán especificaciones de cómo deberán ser los parámetros y la aplicación deberá generar problemas que cumplan
con estas delimitaciones.
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.

Uso:
python3 generator.py [-h] PROBLEMA ARCHIVO PARÁMETROS

Donde:
> El parámetro -h es opcional y muestra la forma de utilización del programa.
> PROBLEMA será el número 1 o 2; 1 si se desea obtener un problema de mochila y 2 si es de alineamiento.
> ARCHIVO será el nombre del archivo con los problemas resultantes.
> PARÁMETROS limitaciones que deberá cumplir el programa.
    > Si se requieren problemas de mochila:
        W N  minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad

        W: Peso soportado por el contenedor.
        N: Cantidad de elementos a trabajar.
        minPeso: Límite inferior para los pesos de los objetos para la mochila.
        maxPeso: Límite superior para asignar los pesos de los elementos.
        minBeneficio: Valor mínimo que puede tener de beneficio un elemento.
        maxBeneficio: Número máximo para el beneficio de los elementos.
        minCantidad: Mínima cantidad disponible de un elemento.
        maxCantidad: Máxima cantidad disponible para un objeto para la mochila.
    *Ejemplo: python3 generator.py 1 salida.txt 50 3 5 15 20 60 3 4

    > Si se necesitan problemas de alineamiento de secuencias:
        largoH1 largoH2

        largoH1: Largo específico de la primera secuencia.
        largoH2: Largo de la segunda secuencia.
    *Ejemplo: python3 generator.py 2 salida.txt 10 10

Salida:
La salida en ambos casos será un archivo .txt capaz de ser utilizado como entrada en el programa solver.py
de este mismo proyecto.

Disponible en: https://github.com/waltermv/IO-Proyecto2-Progra-Dinamica
Este software se encuentra bajo licencia: GPLv3
'''

import sys
from knapsack_generator import knapsack_generator
from sequences_generator import sequences_generator

def help():
    print("Autor: Walter Morales Vásquez\n\
Email: waltermvgit@gmail.com\n\n\
Programa para generar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.\n\
Se recibirán especificaciones de cómo deberán ser los parámetros y la aplicación deberá generar problemas que cumplan\n\
con estas delimitaciones.\n\
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo\n\
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.\n\n\
Uso:\n\
python3 generator.py [-h] PROBLEMA ARCHIVO PARÁMETROS\n\
Donde:\n\
> El parámetro -h es opcional y muestra la forma de utilización del programa.\n\
> PROBLEMA será el número 1 o 2; 1 si se desea resolver un problema de mochila y 2 si es de alineamiento.\n\
> ARCHIVO será el nombre del archivo con los problemas resultantes.\n\
> PARÁMETROS limitaciones que deberá cumplir el programa.\n\
    > Si se requieren problemas de mochila:\n\
        W N  minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad\n\n\
        W: Peso soportado por el contenedor.\n\
        N: Cantidad de elementos a trabajar.\n\
        minPeso: Límite inferior para los pesos de los objetos para la mochila.\n\
        maxPeso: Límite superior para asignar los pesos de los elementos.\n\
        minBeneficio: Valor mínimo que puede tener de beneficio un elemento.\n\
        maxBeneficio: Número máximo para el beneficio de los elementos.\n\
        minCantidad: Mínima cantidad disponible de un elemento.\n\
        maxCantidad: Máxima cantidad disponible para un objeto para la mochila.\n\
    *Ejemplo: python3 generator.py 1 salida.txt 50 3 5 15 20 60 3 4\n\n\
    > Si se necesitan problemas de alineamiento de secuencias:\n\
        largoH1 largoH2\n\n\
        largoH1: Largo específico de la primera secuencia.\n\
        largoH2: Largo de la segunda secuencia.\n\
    *Ejemplo: python3 generator.py 2 salida.txt 10 10\n\n\
Salida:\n\
La salida en ambos casos será un archivo .txt capaz de ser utilizado como entrada en el programa solver.py\n\
de este mismo proyecto.\n\n\
Disponible en: https://github.com/waltermv/IO-Proyecto2-Progra-Dinamica\n\
Este software se encuentra bajo licencia: GPLv3")

def main(args):
    if len(args) < 2:
        print("Uso: python3 generator.py [-h] PROBLEMA ARCHIVO PARÁMETROS")
        exit(1)

    if "-h" in args:
        help()
        exit(0)

    knapsack = False

    if args[1] == "1":
        knapsack = True

    file_path = args[2]

    if knapsack:
        if len(args) != 11:
            print("Uso: python3 generator.py PROBLEMA ARCHIVO \
            W N minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad")
            exit(1)

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
            print("Uso: python3 generator.py PROBLEMA ARCHIVO largoH1 largoH2")
            exit(1)

        length1 = int(args[3])
        length2 = int(args[4])

        sequences_generator(file_path, length1, length2)

if __name__ == '__main__':
    main(sys.argv)