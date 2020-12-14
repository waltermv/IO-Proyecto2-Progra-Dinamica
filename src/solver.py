# -*- coding: utf-8 -*-

'''
Autor: Walter Morales Vásquez
Email: waltermvgit@gmail.com

Programa para solucionar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.
Para la resolver cada uno de los problemas se brindan dos opciones: utilizar un algoritmo de fuerza bruta o uno de
programación dinámica (esto deberá ser especificado en los parámetros de la aplicación).
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.

Uso:
python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO

Donde:
> El parámetro -h es opcional y muestra la forma de utilización del programa.
> PROBLEMA será el número 1 o 2; 1 si se desea resolver un problema de mochila y 2 si es de alineamiento.
> ALGORITMO es un valor de 1 o 2; si se desea solucionar mediante fuerza bruta 1 y si se requiere usar
programación dinámica 2.
> ARCHIVO es el nombre del archivo de entrada el cual se obtendrán los datos del problema. Deberá encontrarse
en el directorio raíz del proyecto.
    > En el caso de que se use mochila:
        - Línea 1: Peso máximo soportado por el contenedor. Ej: 50
        - Línea i: Elemento en la posición i (peso, beneficio, cantidad). Ej: 5,20,4
                                                                              15,50,3
                                                                              10,60,3

    > En el caso de ser un problema de alineamiento:
        - Línea 1: Primera secuencia a alinear. Ej: ATTGTGATCC
        - Línea 2: Segunda secuencia a alinear. Ej: TTGCATCGGC

Salida:
> En el caso de mochila:
    - Línea 1: Beneficio máximo posible. Ej: 260
    - Línea j: Posición original del artículo: i, cantidad de unidades. Ej: 1,4
                                                                            3,3

> En el caso de alineamiento:
    - Línea 1: Indica el "score" final de los alineamientos. Ej: -2
    - Línea 2: Hilera resultado para la primer secuencia.
    - Línea 3: Hilera resultado para la segunda secuencia.
    * En el caso de que se utilizara programación dinámica para resolver el problema, el programa generará
    un archivo csv con la matriz resultado, se utilizará el nombre del archivo de donde se obtuvieron los datos
    junto con el sufijo "_solution" para este fin.

Disponible en: https://github.com/waltermv/IO-Proyecto2-Progra-Dinamica
Este software se encuentra bajo licencia: GPLv3
'''

import sys

from input import input_class
from knapsack_solver import knapsack_brute_force_solver, knapsack_dynamic_solver
from sequences_solver import sequences_brute_force_solver, sequences_dynamic_solver

# Función para imprimir la información del programa generador de problemas de contenedor y de alineamiento de secuencias.
def help():
    print("Autor: Walter Morales Vásquez\n\
Email: waltermvgit@gmail.com\n\n\
Programa para solucionar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.\n\
Para la resolver cada uno de los problemas se brindan dos opciones: utilizar un algoritmo de fuerza bruta o uno de\n\
programación dinámica (esto deberá ser especificado en los parámetros de la aplicación).\n\
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo\n\
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.\n\n\
Uso:\n\
python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO\n\n\
Donde:\n\
> El parámetro -h es opcional y muestra la forma de utilización del programa.\n\
> PROBLEMA será el número 1 o 2; 1 si se desea resolver un problema de mochila y 2 si es de alineamiento.\n\
> ALGORITMO es un valor de 1 o 2; si se desea solucionar mediante fuerza bruta 1 y si se requiere usar\n\
programación dinámica 2.\n\
> ARCHIVO es el nombre del archivo de entrada el cual se obtendrán los datos del problema. Deberá encontrarse\n\
en el directorio raíz del proyecto.\n\
    > En el caso de que se use mochila:\n\
        - Línea 1: Peso máximo soportado por el contenedor. Ej: 50\n\
        - Línea i: Elemento en la posición i (peso, beneficio, cantidad). Ej: 5,20,4\n\
                                                                              15,50,3\n\
                                                                              10,60,3\n\n\
    > En el caso de ser un problema de alineamiento:\n\
        - Línea 1: Primera secuencia a alinear. Ej: ATTGTGATCC\n\
        - Línea 2: Segunda secuencia a alinear. Ej: TTGCATCGGC\n\n\
Salida:\n\
> En el caso de mochila:\n\
    - Línea 1: Beneficio máximo posible. Ej: 260\n\
    - Línea j: Posición original del artículo: i, cantidad de unidades. Ej: 1,4\n\
                                                                            3,3\n\n\
> En el caso de alineamiento:\n\
    - Línea 1: Indica el \"score\" final de los alineamientos. Ej: -2\n\
    - Línea 2: Hilera resultado para la primer secuencia.\n\
    - Línea 3: Hilera resultado para la segunda secuencia.\n\
    * En el caso de que se utilizara programación dinámica para resolver el problema, el programa generará\n\
    un archivo csv con la matriz resultado, se utilizará el nombre del archivo de donde se obtuvieron los datos\n\
    junto con el sufijo \"_solution\" para este fin.\n\n\
Disponible en: https://github.com/waltermv/IO-Proyecto2-Progra-Dinamica\n\
Este software se encuentra bajo licencia: GPLv3")

# Función principal del módulo solucionador de problemas de contenedor y de alineamiento de secuencias.
def main(args):
    # Se comprueba la cantidad de argumentos recibidos.
    if len(args) < 2:
        print("Uso: python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO")
        exit(1)

    # Si se recibió un "-h" en algún lugar de los argumentos del programa se imprime la explicación del funcionamiento
    # del programa.
    if "-h" in args:
        help()
        exit(0)         # Se termina con la ejecución de la aplicación.

    # Se comprueba el largo de los argumentos.
    if len(args) != 4:
        print("Uso: python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO")
        exit(1)

    knapsack = False    # Parámetro que indica si se realizará un problema de mochila o de alineamiento de secuencias.

    if args[1] == "1":      # Se comprueba si el primer argumento es 1 o es 2.
        knapsack = True     # Si es 1 se resolverá un problema de mochila.

    brute_force = False     # Parámetro que dice si se deberá utilizar la fuerza bruta o la programación dinámica para
                            # resolver el problema.

    if args[2] == "1":      # Se comprueba si se requiere utilizar fuerza bruta.
        brute_force = True  # Si el argumento que especifica esto es 1 entonces se utilizará fuerza bruta.

    file_path = args[3]     # Ruta del archivo donde se encuentran los datos del problema.
    input_var = input_class(knapsack, file_path)    # Se obtiene la información del problema.

    if(knapsack):           # Si se desea resolver un problema de mochila.
        if(brute_force):    # Si solicitaron utilizar fuerza bruta.
            answer = knapsack_brute_force_solver(input_var)     # Se llama a la función capaz de resolver el problema.
        else:               # Se requiere utilizar programación dinámica.
            answer = knapsack_dynamic_solver(input_var)         # Se llama a la función capaz de resolver el problema.

        print(answer[0])    # Se imprime el valor máximo que se puede obtener de este contenedor con los elementos
                            # especificados.
        for element in answer[1:]:      # Por cada elemento en la respuesta.
            print(str(element[0])+','+str(element[1]))  # Se imprimen sus datos.
    else:                   # Si debemos resolver un problema de alineamiento de secuencias.
        if (brute_force):   # Si solicitaron utilizar fuerza bruta.
            answer = sequences_brute_force_solver(input_var)    # Se llama a la función capaz de resolver el problema.
        else:               # Requerimos utilizar programación dinámica.
            answer = sequences_dynamic_solver(input_var)        # Se llama a la función capaz de resolver el problema.

        print("Score final: " + str(answer[0]))     # Se imprime la puntuación final de la alineación.
        print("Hilera 1: " + str(answer[1]))        # Imprimimos la primera secuencia resultado.
        print("Hilera 2: " + str(answer[2]))        # Se imprime la segunda hilera resultante.

# Para definir la función principal del programa.
if __name__ == '__main__':
    main(sys.argv)