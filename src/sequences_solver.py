# -*- coding: utf-8 -*-

import itertools

match = 1               # Valor para un "match" en los algoritmo.
missmatch = -1          # Número que representa un "missmatch" de caracteres.
gap = -2                # Número por si se encuentra un gap al comprobar dos caracteres.
diagonal = 1 << 0       # Bit que indica donde si existe un enlace diagonal.
upper = 1 << 1          # Bit para saber si hay un enlace hacía arriba.
left = 1 << 2           # Bit utilizado para conocer si existe una unión con la celda de la izquierda.

# Función llamada para resolver el problema de alineamiento de secuencias con fuerza bruta.
def sequences_brute_force_solver(input):
    return brute_force(input.sequence1, input.sequence2)    # Se retorna la respuesta.

# Método que resuelve el problema de alineamiento al comprobar todas las posibles combinaciones de una secuencia con gaps
# con otra de también podría poseer gaps. No termina hasta comprobar con cada una de las posibles combinaciones.
def brute_force(sequence1, sequence2):
    max_score = -9999           # Puntuación para las combinaciones máxima encontrada.
    current_sequence1 = ""      # Variables que almacenan el mejor par de secuencias encontradas.
    current_sequence2 = ""

    length1 = len(sequence1)    # Largo de la primera secuencia.
    length2 = len(sequence2)    # Largo de la segunda secuencia.
    min_length = min(length1, length2)  # Valor mínimo del largo de las secuencias.

    difference1 = 0             # Variables que almacenan la diferencia de espacio que existe entre las
    difference2 = 0             # dos secuencias.
    if length1 < length2:       # Si el valor de la secuencia 2 es mayor, se deberán añadir vacíos a la primera secuencia.
        difference1 = length2 - length1
    else:                       # En caso contrario se deberán añadir vacíos a la segunda secuencia.
        difference2 = length1 - length2

    # Se itera por la cantidad de vacíos que se deberán colocar.
    for i in range(min_length+1):
        new_combinations1 = get_combinations(sequence1, length1, difference1+i)     # Se obtienen las posibles combinaciones
                                                                                    # de la primera secuencia con la
                                                                                    # cantidad de gaps recibida.
        new_combinations2 = get_combinations(sequence2, length2, difference2+i)     # Posibles combinaciones de la
                                                                                    # segunda hilera tomando en cuenta
                                                                                    # los vacíos.
        for element1 in new_combinations1:          # Por cada elemento en las combinaciones de la primera.
            for element2 in new_combinations2:      # Por cada elemento en las combinaciones de la segunda.
                score = sequence_score(element1, element2)  # Se calcula la puntuación de las dos secuencias.
                if score > max_score:               # Si la puntuación es mayor a la que se tenía anteriormente.
                    max_score = score               # Guardamos la puntuación.
                    current_sequence1 = element1    # Se almacena la primera hilera.
                    current_sequence2 = element2    # Almacenamos la segunda secuencia.

    return [max_score, current_sequence1, current_sequence2]    # Se retorna el resultado en una lista.

# Función para obtener las posibles combinaciones de una secuencia al colocarle vacíos. El orden de los caracteres de la
# secuencia no es alterado. Se recibe la secuencia, el largo de la misma y los vacíos a colocar.
def get_combinations(sequence, length, quantity_gaps):
    # Colocamos "{}" donde deberían estar los caracteres de la secuencia y los espacios vacíos que faltan. Se realiza
    # una permitación de lo anterior y se transforma el resultado a string.
    combinations = sorted({"".join(p) for p in itertools.permutations(["{}"]*length + ["_"]*quantity_gaps)})
    # Ahora podemos poner los caracteres originales donde deberian estar aprovechándonos de la función "format" y de los
    # "{}" anteriormente colocados.
    return [element.format(*list(sequence)) for element in combinations]    # Se da el resultado.

# Método para evaluar que tan parecidos son dos pares de secuencias. Ambas secuencias son del mismo tamaño gracias a los
# vacíos.
def sequence_score(sequence1, sequence2):
    score = 0           # La puntuación inicial es 0.
    for i in range(len(sequence1)):     # Se itera sobre el largo de la primera.
        if sequence1[i] == "_" or sequence2[i] == "_":  # Si existe un vacío en la posición i de alguna de las dos
            score += gap                                # hileras, se le suma a la puntuación el valor del "gap".
        elif sequence1[i] == sequence2[i]:              # Si las secuencias en la posición i son iguales, se le suma
            score += match                              # el valor de un "match".
        else:                                           # Si ninguna de las condiciones anteriores es correcta se le
            score += missmatch                          # suma a la puntuación un "missmatch".
    return score                        # Se da el resultado.

# Función llamada para resolver el problema de alineamiento de secuencias con programación dinámica.
def sequences_dynamic_solver(input):
    return dynamic(input.sequence1, input.sequence2, input.file_path)

# Implementación del alineamiento global creado por Needleman y Wunsch. Se basa en comparar en una matriz si sería mejor
# asumir el valor de no colocar ningún vacío, colocar un vacío en la primera secuencia o colocar un "gap" en la segunda.
def dynamic(sequence1, sequence2, file_name):
    length_seq1 = len(sequence1) + 1    # Cantidad de filas en la matriz.
    length_seq2 = len(sequence2) + 1    # Cantidad de columnas en la matriz.
    matrix = [[[0, 0] for i in range(length_seq2)] for j in range(length_seq1)] # Se crea la matriz llena de ceros.

    for i in range(1, max(length_seq1, length_seq2)):   # Se recorre por el máximo de alguno de los dos valores.
        if i < length_seq2:             # Si no se ha sobrepasado el límite de columnas.
            matrix[0][i][0] = -2 * i    # Se le asigna a las celdas de la primera fila el valor de -2*i
            matrix[0][i][1] |= left     # Enlazamos la celda con la de su izquierda.
        if i < length_seq1:             # Si no se ha superado el límite de filas.
            matrix[i][0][0] = -2 * i    # Asignamos a las filas de la primera columna el valor de -2*i
            matrix[i][0][1] |= upper    # Se enlaza la celda con la que se encuentra arriba de esta.

    for i in range(1, length_seq1):         # Recorremos la matriz
        for j in range(1, length_seq2):
            diagonal_result = matrix[i - 1][j - 1][0] + char_score(sequence1[i - 1], sequence2[j - 1])  # Se calcula el
                                                            # resultado de no poner ningún vacío, esto será más beneficioso
                                                            # si las secuencias en esa posición coinciden.
            upper_result = matrix[i - 1][j][0] + gap        # Se calcula el valor de colocar un gap en la segunda hilera.
            left_result = matrix[i][j - 1][0] + gap         # Calculamos el valor de colocar un vacío en la primera
                                                            # secuencia.
            matrix[i][j][0] = max(diagonal_result, upper_result, left_result)   # El valor de la celda será el mayor de
                                                                                # entre los números calculados.
            if diagonal_result == matrix[i][j][0]:          # Si el resultado es igual al valor de la operación con la.
                matrix[i][j][1] |= diagonal                 # diagonal, se realiza un enlace con esta.
            if upper_result == matrix[i][j][0]:             # En caso de que el resultado sea igual al valor de la
                matrix[i][j][1] |= upper                    # operación "upper", se enlaza con la celda de arriba.
            if left_result == matrix[i][j][0]:              # Si se eligió el valor de la operación "left", se enlaza
                matrix[i][j][1] |= left                     # con la celda de la izquierda.

    answer = matrix[length_seq1 - 1][length_seq2 - 1]       # La respuesta será el último valor de la matriz.
    answer_sequence1 = ""           # Variables que mantendrán las secuencias resultado.
    answer_sequence2 = ""

    i = length_seq1 - 1             # Índices para iterar en la matriz y buscar las secuencias resultado.
    j = length_seq2 - 1

    while i != 0 or j != 0:         # Mientras alguno de los índices no sea cero.
        if matrix[i][j][1] & diagonal:      # Si existe un enlace diagonal en esta celda.
            answer_sequence1 = sequence1[i - 1] + answer_sequence1  # Se coloca el caracter que corresponde a la fila i
                                                                    # al comienzo de la hilera respuesta 1.
            answer_sequence2 = sequence2[j - 1] + answer_sequence2  # Colocamos el caracter que corresponde a la columna
                                                                    # j al comienzo de la hilera respuesta 1.
            i -= 1      # Se disminuyen en 1 ambos índices.
            j -= 1
        elif matrix[i][j][1] & upper:       # Si existe un enlace hacía la celda de arriba.
            answer_sequence1 = sequence1[i - 1] + answer_sequence1  # Se coloca el caracter que corresponde a la fila i
                                                                    # al comienzo de la hilera respuesta 1.
            answer_sequence2 = "_" + answer_sequence2               # Colocamos un "gap" al comienzo de la hilera
                                                                    # respuesta 2.
            i -= 1      # Disminuimos en 1 el valor de i.
        else:                               # Si el enlace está hacía la izquierda.
            answer_sequence1 = "_" + answer_sequence1               # Colocamos un "gap" al comienzo de la primera
                                                                    # hilera respuesta.
            answer_sequence2 = sequence2[j - 1] + answer_sequence2  # Colocamos el caracter que corresponde a la columna
                                                                    # j al comienzo de la hilera respuesta 1.
            j -= 1      # Se disminuye en 1 el valor de j.

    write_matrix_in_file(matrix, file_name)                 # Escribimos el archivo con la matriz respuesta.

    return [answer[0], answer_sequence1, answer_sequence2]  # Retornamos la respuesta en una lista.

# Función para calcular la puntuación entre dos caracteres sin "gaps".
def char_score(char1, char2):
    if char1 == char2:          # Si los caracteres son iguales se retorna un "match".
        return match
    return missmatch            # En caso contrario se retorna un "missmatch".

# Función para escribir el archivo csv con la matriz solución. Recibe la matriz solución a imprimir y el nombre del
# archivo a generar.
def write_matrix_in_file(matrix, file_name):
    file = open("../"+file_name+"_solution.csv", "w")  # Se crea el archivo de salida en modo escritura.
    # Se recorre la matriz solución.
    for i in matrix:
        for j in i:
            if j[1] & diagonal:         # Si existe un enlace diagonal se escribe una flecha que lo indique.
                file.write('↖')
            if j[1] & upper:            # Si existe un enlace hacía arriba se indica con una flecha.
                file.write('↑')
            if j[1] & left:             # Si hay un enlace hacía la izquierda se utiliza una flecha que apunta hacía
                file.write('←')         # izquierda.
            file.write(' ' + str(j[0]) + ',')   # Se escribe el valor de la celda.
        file.write('\n')                # Colocamos un salto de línea.

    file.close()        # Cerramos el archivo.

# Utilizado para comprobar el funcionamiento de la función "get_combinations"
'''
secuencia = "GTCAA"
espacios = 2
lista = get_combinations(secuencia, len(secuencia), espacios)
print(str(len(lista))+" combinaciones obtenidas de "+secuencia+" con "+str(espacios)+" espacios\n")
for i in lista:
    print(i)
'''
