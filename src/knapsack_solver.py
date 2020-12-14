# -*- coding: utf-8 -*-

items_list = []     # Lista que almacenará a los elementos a colocar en el contenedor.
weight = 0          # Índice que indica la posición donde se encuentra el peso de un elemento.
value = 1           # Índice para obtener el valor de un elemento.
identifier = 2      # Indicador de dónde se encuentra el identificador del objeto.

# Función llamada para resolver el problema de contenedor con fuerza bruta.
def knapsack_brute_force_solver(input):
    items_list[:] = input.items_list        # Se almacena la lista de elementos de manera global.
    answer_list = []                        # Lista donde se encontrará la respuesta.
    answer = brute_force(input.max_weight, len(items_list)-1, answer_list)  # Se recibe el máximo valor beneficio.
    answer_list = [[i, answer_list.count(i)] for i in set(answer_list)]     # Se define el formato para la respuesta.
                                                                            # Identificador del artículo y cantidad.
    return [answer] + answer_list           # Se retorna la respuesta.

# Función que busca la solución óptima para el problema de mochila dado. Utiliza la recursión para verificar que pasaría
# si se almacena cualquier conjunto de elementos posibles en el depósito y retorna el valor beneficio máximo encontrado.
def brute_force(knapsack_weight, item_position, answer_list):
    # Si ya se ha pasado el peso máximo del contenedor, se retorna un número muy grande, en este caso -999999.
    if knapsack_weight < 0:
        return -999999

    # Si ya no quedan elementos en la lista o ya nos quedamos sin capacidad en la mochila, retornamos 0.
    if item_position < 0 or knapsack_weight == 0:
        return 0

    item = items_list[item_position]    # Se obtiene al elemento actual a partir de la lista y del índice actual.
    # Primer caso, se inserta al elemento en la mochila y se aumenta el valor del beneficio en el beneficio de colocar
    # al elemento. Se guarda al elemento en una lista y se manda como parámetro para después recuperarla.
    include_list = answer_list+[item[identifier]]
    include = item[value] + brute_force(knapsack_weight - item[weight], item_position - 1, include_list)

    # Segundo caso, el elemento es ignorado y no se realiza ningún cambio en el beneficio de la mochila.
    exclude_list = answer_list
    exclude = brute_force(knapsack_weight, item_position - 1, exclude_list)

    # Si el valor de incluir el elemento resultó ser mayor que el de no incluirlo, se retorna el valor obtenido en esta
    # recursión como respuesta.
    if include > exclude:
        answer_list[:] = include_list   # Se guarda la lista resultado en la lista respuesta recibida.
        return include                  # Retornamos el valor máximo.
    # Si resultó mejor el resultado de excluir al elemento se retorna la respuesta de esta recursión.
    answer_list[:] = exclude_list       # Se guarda la lista resultado en la lista respuesta recibida.
    return exclude                      # Retornamos el valor máximo.

# Función llamada para resolver el problema de contenedor mediante programación dinámica.
def knapsack_dynamic_solver(input):
    items_list[:] = input.items_list    # Se guardan los elementos a comprobar en la lista global.
    return dynamic(input.max_weight, len(items_list)-1, input.file_path)     # Se retorna el resultado.

# Método para encontrar la respuesta a un problema de mochila mediante la programación dinámica. Se basa en colocar en
# una matriz de tamaño 'W' (peso máximo soportado por el contenedor) por 'N' (número de elementos a comprobar) el valor
# de colocar elementos de manera acumulativa. Se busca que la casilla (i, j) indique el valor beneficio máximo que se ha
# utilizado para rellenar el depósito cuando es de tamaño j tomando en cuenta todos los objetos hasta el elemento de
# índice i.
def dynamic(knapsack_weight, items_quantity, file_name):
    matrix = [[0 for i in range(knapsack_weight + 1)] for j in range(items_quantity + 1)]   # Se crea la matriz.

    for item_position in range(items_quantity + 1):      # Se itera sobre la matriz.
        for actual_weight in range(knapsack_weight + 1):
            item = items_list[item_position]            # Se obtiene al elemento que corresponde a esta iteración.
            if (item[weight] > actual_weight):              # Si no es posible para el elemento ser agregado en la
                                                            # presente celda de la matriz.
                matrix[item_position][actual_weight] = matrix[item_position - 1][actual_weight] # Se utiliza el valor
                                                                                                # anterior
            else:                                           # Si es posible.
                if (item[value] + matrix[item_position - 1][actual_weight - item[weight]]) > matrix[item_position - 1][
                    actual_weight]:                         # Si el valor de insertar al elemento es mayor del que se
                                                            # estaba manejando.
                    matrix[item_position][actual_weight] = item[value] + matrix[item_position - 1][ # Se agrega el nuevo
                        actual_weight - item[weight]]                                               # valor.
                else:
                    matrix[item_position][actual_weight] = matrix[item_position - 1][actual_weight] # Se utiliza el valor
                                                                                                    # anterior

    answer = matrix[items_quantity][knapsack_weight]    # La respuesta será el último elemento de la matriz.
    answers_list = []                                   # Lista para almacenar los datos de los elementos que han sido
                                                        # insertados.
    # Recorremos la matriz verificando cuales elementos se han utilizado para la solución
    while items_quantity != 0:          # Se recorre las filas de la matriz porque son las que representan a los elementos.
        if matrix[items_quantity][knapsack_weight] != matrix[items_quantity - 1][knapsack_weight]:  # Si cambia el valor
                                                            # beneficio al pasar de la fila actual y la de atrás es
                                                            # porque se ha insertado al elemento.
            if answers_list == []:      # Si la lista era vacía.
                answers_list.append([items_list[items_quantity-1][identifier], 1])  # Se inserta al elemento.
            else:
                if items_list[items_quantity-1][identifier] == answers_list[-1][0]: # Si el identificador era el mismo
                                                            # del anterior es porque era el mismo.
                    answers_list[-1][1] += 1                # Se aumenta en 1 la cantidad del elemento.
                else:
                    answers_list.append([items_list[items_quantity-1][identifier], 1])  # Se agrega al elemento como
                                                                                        # nuevo.
            knapsack_weight -= items_list[items_quantity-1][weight]     # Se le resta al tamaño de la mochila el tamaño
                                                                        # del elemento recién identificado.
        items_quantity -= 1         # Disminuimos en 1 el contador de elementos.

    write_matrix_in_file(matrix, file_name)
    answers_list.reverse()          # Se da la lista al revés porque se leyó de abajo hacía arriba.
    return [answer] + answers_list  # Retornamos la respuesta.

# Función para escribir el archivo csv con la matriz solución. Recibe la matriz solución a imprimir y el nombre del
# archivo a generar.
def write_matrix_in_file(matrix, file_name):
    file = open("../"+file_name+"_solution.csv", "w")  # Se crea el archivo de salida en modo escritura.
    # Se recorre la matriz solución.
    for i in matrix:
        for j in i:
            file.write(str(j) + ',')     # Se escribe el valor de la celda.
        file.write('\n')                    # Colocamos un salto de línea.

    file.close()        # Cerramos el archivo.