# -*- coding: utf-8 -*-

import itertools

match = 1
missmatch = -1
gap = -2
diagonal = 1 << 0
upper = 1 << 1
left = 1 << 2

def sequences_brute_force_solver(input):
    return brute_force(input.sequence1, input.sequence2)

def brute_force(sequence1, sequence2):
    max_score = -9999
    current_sequence1 = ""
    current_sequence2 = ""

    length1 = len(sequence1)
    length2 = len(sequence2)
    #max_length = max(length1, length2)
    min_length = min(length1, length2)

    difference1 = 0
    difference2 = 0
    if length1 < length2:
        difference1 = length2 - length1
    else:
        difference2 = length1 - length2

    for i in range(min_length+1):
        new_combinations1 = get_combinations(sequence1, length1, difference1+i)
        new_combinations2 = get_combinations(sequence2, length2, difference2+i)
        for element1 in new_combinations1:
            for element2 in new_combinations2:
                score = sequence_score(element1, element2)
                if score > max_score:
                    max_score = score
                    current_sequence1 = element1
                    current_sequence2 = element2

    return [max_score, current_sequence1, current_sequence2]

def get_combinations(sequence, length, quantity_gaps):
    combinations = sorted({"".join(p) for p in itertools.permutations(["{}"]*length + ["_"]*quantity_gaps)})
    return [element.format(*list(sequence)) for element in combinations]
    #combinations = [element.format(*list(sequence)) for element in combinations]

def sequence_score(sequence1, sequence2):
    score = 0
    for i in range(len(sequence1)):
        if sequence1[i] == "_" or sequence2[i] == "_":
            score += gap
        elif sequence1[i] == sequence2[i]:
            score += match
        else:
            score += missmatch
    return score

#Algoritmo de alineamiento global creado por Needleman y Wunsch
def sequences_dynamic_solver(input):
    return dynamic(input.sequence1, input.sequence2, input.file_path)

def dynamic(sequence1, sequence2, file_name):
    length_seq1 = len(sequence1) + 1
    length_seq2 = len(sequence2) + 1
    matrix = [[[0, 0] for i in range(length_seq2)] for j in range(length_seq1)]

    for i in range(1, max(length_seq1, length_seq2)):
        if i < length_seq2:
            matrix[0][i][0] = -2 * i
            matrix[0][i][1] |= left
        if i < length_seq1:
            matrix[i][0][0] = -2 * i
            matrix[i][0][1] |= upper

    for i in range(1, length_seq1):
        for j in range(1, length_seq2):
            diagonal_result = matrix[i - 1][j - 1][0] + char_score(sequence1[i - 1], sequence2[j - 1])
            upper_result = matrix[i - 1][j][0] + gap
            left_result = matrix[i][j - 1][0] + gap
            matrix[i][j][0] = max(diagonal_result, upper_result, left_result)
            if diagonal_result == matrix[i][j][0]:
                matrix[i][j][1] |= diagonal
            if upper_result == matrix[i][j][0]:
                matrix[i][j][1] |= upper
            if left_result == matrix[i][j][0]:
                matrix[i][j][1] |= left

    answer = matrix[length_seq1 - 1][length_seq2 - 1]
    answer_sequence1 = ""
    answer_sequence2 = ""

    i = length_seq1 - 1
    j = length_seq2 - 1

    #print(sequence1, sequence2)

    while i != 0 or j != 0:
        if matrix[i][j][1] & diagonal:
            answer_sequence1 = sequence1[i - 1] + answer_sequence1
            answer_sequence2 = sequence2[j - 1] + answer_sequence2
            i -= 1
            j -= 1
        elif matrix[i][j][1] & upper:
            answer_sequence1 = sequence1[i - 1] + answer_sequence1
            answer_sequence2 = "_" + answer_sequence2
            i -= 1
        else:
            answer_sequence1 = "_" + answer_sequence1
            answer_sequence2 = sequence2[j - 1] + answer_sequence2
            j -= 1

    print_matrix(matrix, file_name)

    return [answer[0], answer_sequence1, answer_sequence2]

def char_score(char1, char2):
    if char1 == char2:
        return match
    return missmatch

def print_matrix(matrix, file_name):
    file = open("../"+file_name+"_solution.csv", "w")  #Crea el archivo de salida
    for i in matrix:
        for j in i:
            if j[1] & diagonal:
                file.write('↖')
            if j[1] & upper:
                file.write('↑')
            if j[1] & left:
                file.write('←')
            file.write(' ' + str(j[0]) + ',')
        file.write('\n')

    file.close()

#print(brute_force("ATTG", "ATTGA"))
dynamic("GTGCC", "AATATGAGTT", "prueba")