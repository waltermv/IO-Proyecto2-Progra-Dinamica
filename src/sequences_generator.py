import random
from datetime import datetime

possible_chars = ["A", "T", "C", "G"]

def sequences_generator(file_path, length1, length2):
    new_file = open("../"+file_path, "w")

    random.seed(datetime.now())
    sequence1 = ""
    for i in range(length1):
        sequence1 += random.choice(possible_chars)

    sequence2 = ""
    for i in range(length2):
        sequence2 += random.choice(possible_chars)

    new_file.write(sequence1+"\n")
    new_file.write(sequence2+"\n")
    print("¡Archivo generado con éxito!")

