# -*- coding: utf-8 -*-

import random
from datetime import datetime

possible_chars = ["A", "T", "C", "G"]       # Lista de posibles caracteres a utilizar para generar un problema.

# Función para generar un problema de alineamiento de secuencias con las posibles bases presentes en el ADN.
# Recibe el nombre del archivo a generar o modificar, el largo de la primera secuencia y el largo de la segunda.
def sequences_generator(file_path, length1, length2):
    new_file = open("../"+file_path, "w")   # Se abre o se crea un archivo con el nombre especificado en modo escritura.

    random.seed(datetime.now())             # Generamos una semilla para el generador de valores random.
    sequence1 = ""                          # Definimos la primera secuencia.
    for i in range(length1):                # Iteramos por el largo de la primera hilera especificada.
        sequence1 += random.choice(possible_chars)  # Se elige un caracter al azar entre los posibles.

    sequence2 = ""                          # Se define la segunda hilera.
    for i in range(length2):                # Por el largo de la segunda hilera especificada.
        sequence2 += random.choice(possible_chars)  # Se elige un caracter al azar entre los posibles.

    new_file.write(sequence1+"\n")          # Se escribe en el archivo la primera hilera.
    new_file.write(sequence2+"\n")          # Escribimos la segunda.

    print("¡Archivo generado con éxito!")   # Se le indica al usuario que se ha terminado.

