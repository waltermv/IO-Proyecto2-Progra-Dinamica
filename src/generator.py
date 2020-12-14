# -*- coding: utf-8 -*-

'''
Autor: Walter Morales Vásquez
Email: waltermvgit@gmail.com

Programa para generar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.
Se recibirán especificaciones de cómo deberán ser los parámetros y la aplicación deberá generar problemas que cumplan
con estas delimitaciones. Para ambos problemas el archivo generado aparecerá en la carpeta raíz del proyecto.
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

# Función para imprimir la información del programa generador de problemas de contenedor y de alineamiento de secuencias.
def help():
    print("Autor: Walter Morales Vásquez\n\
Email: waltermvgit@gmail.com\n\n\
Programa para generar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.\n\
Se recibirán especificaciones de cómo deberán ser los parámetros y la aplicación deberá generar problemas que cumplan\n\
con estas delimitaciones. Para ambos problemas el archivo generado aparecerá en la carpeta raíz del proyecto.\n\
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

# Función principal del módulo generador de problemas de contenedor y de alineamiento de secuencias.
def main(args):
    # Se comprueba la cantidad de argumentos recibidos.
    if len(args) < 2:
        print("Uso: python3 generator.py [-h] PROBLEMA ARCHIVO PARÁMETROS")
        exit(1)

    # Si existe un "-h" en algún lado de los argumentos se imprime la información del programa.
    if "-h" in args:
        help()
        exit(0)             # Se termina con la ejecución de la aplicación.

    knapsack = False        # Parámetro que indica si se realizará un problema de mochila o de alineamiento de secuencias.

    if args[1] == "1":      # Se comprueba si el primer argumento es 1 o es 2.
        knapsack = True     # Si es 1 se creará un problema de mochila.

    file_path = args[2]     # Se recibe el path en donde se generará el archivo resultado.

    if knapsack:            # Si piden un problema de mochila.
        # Comprobamos si es correcta la cantidad de argumentos.
        if len(args) != 11:
            print("Uso: python3 generator.py PROBLEMA ARCHIVO \
            W N minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad")
            exit(1)

        weight = args[3]                # Peso máximo de la mochila.
        quantity = int(args[4])         # Cantidad de elementos para comprobar.
        min_weight = int(args[5])       # Límite inferior para definir el peso de los elementos.
        max_weight = int(args[6])       # Límite superior para el peso de los elementos.
        min_value = int(args[7])        # Beneficio mínimo de colocar al elemento en el deposito.
        max_value = int(args[8])        # Máximo que se obtiene de colocar al elemento en el contenedor.
        min_quantity = int(args[9])     # Mínima cantidad en el inventario del elemento.
        max_quantity = int(args[10])    # Cantidad máxima que puede estar en el inventario.

        # Se llama a la función capaz de generar problemas de mochila.
        knapsack_generator(file_path, weight, quantity, min_weight, max_weight, min_value, max_value, min_quantity, max_quantity)
    else:                   # Si solicitaron un problema de alineamiento de secuencias.
        if len(args) != 5:  # Se comprueba la cantidad de parámetros.
            print("Uso: python3 generator.py PROBLEMA ARCHIVO largoH1 largoH2")
            exit(1)

        length1 = int(args[3])      # Largo de la primera hilera.
        length2 = int(args[4])      # Largo de la segunda secuencia.

        # Se llama al método generador de problemas de alineamiento.
        sequences_generator(file_path, length1, length2)

# Para definir la función principal del programa.
if __name__ == '__main__':
    main(sys.argv)