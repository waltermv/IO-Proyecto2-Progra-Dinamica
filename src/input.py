# -*- coding: utf-8 -*-

# Clase que almacena los datos recibidos del archivo pasado como parámetro para resolver un problema.
class input_class:
    def __init__(self, knapsack, file_path):
        self.file_path = file_path              # Se guarda el nombre del archivo.
        if(knapsack):                           # Si es de mochila se llama a la función capaz de analizar el archivo.
            self.read_knapsack_input(file_path)
        else:                                   # Si no se reciben los datos para un problema de alineamiento.
            self.read_sequences_input(file_path)

    # Función para obtener los datos de un problema de contenedor a partir de un archivo.
    def read_knapsack_input(self, file_path):
        file = open("../"+file_path, "r")       # Se abre el archivo en modo lectura.
        line = file.readline()                  # Leemos la primera línea.

        self.max_weight = int(line)             # Guardamos el peso máximo soportado por el contenedor.
        self.items_list = []                    # Se define la lista que guardará a los elementos.

        identifier = 1                          # Se inicia el identificador para los elementos.
        # Las líneas del archivo deberán especificar en este orden: el peso, el beneficio y la cantidad.
        for line in file:
            line = list(map(int, line.split(',')))  # Separamos los datos por la coma.
            for i in range(line[2]):                # Por cada cantidad en el inventario se añade uno a la lista.
                self.items_list.append(line[:2]+[identifier])   # Se utiliza el mismo identificador.
            identifier += 1                         # Aumentamos el identificador.

        file.close()            # Cerramos el archivo del que estabamos leyendo.

    # Función para leer los datos de un archivo que define un problema de alineamiento de hileras.
    def read_sequences_input(self, file_path):
        file = open("../"+file_path, "r")       # Se abre el archivo en modo lectura.

        self.sequence1 = file.readline().rstrip('\n')   # Leemos la primera línea y le removemos el salto de línea.
        self.sequence2 = file.readline().rstrip('\n')   # Se lee la segunda línea y, de igual manera, se le quita
                                                        # el salto de línea.