# -*- coding: utf-8 -*-

import random
from datetime import datetime

# Función para generar un archivo con los datos de un problema de mochila.
# Se recibe el nombre del archivo a generar, el peso soportado por el contenedor, la cantidad de elementos a trabajar,
# el límite inferior para los pesos de los objetos para la mochila, el límite superior para asignar los pesos de los
# elementos, el valor mínimo que puede tener de beneficio un elemento, el número máximo para el beneficio de los
# elementos, la mínima cantidad disponible de un elemento y la máxima cantidad disponible para un objeto para la mochila.
def knapsack_generator(file_path, weight, quantity, min_weight, max_weight, min_value, max_value, min_quantity, max_quantity):
    new_file = open("../"+file_path, "w")   # Se abre o se crea un archivo con el nombre especificado en modo escritura.
    new_file.write(weight+"\n")             # Se escribe el peso soportado por el contenedor.

    random.seed(datetime.now())             # Generamos una semilla para el generador de números random.
    for i in range(quantity):               # Por la cantidad indicada de elementos:
        new_weight = random.randint(min_weight, max_weight)         # Se define un peso al elemento.
        new_value = random.randint(min_value, max_value)            # Generamos un valor para el elemento.
        new_quantity = random.randint(min_quantity, max_quantity)   # Definimos la cantidad en el inventario.
        new_file.write("{},{},{}\n".format(new_weight, new_value, new_quantity))    # Se escribe en el archivo.

    print("¡Archivo generado con éxito!")   # Se le indica al usuario que se ha terminado.