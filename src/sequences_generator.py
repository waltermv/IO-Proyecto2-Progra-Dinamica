import random

possible_chars = ["A", "T", "C", "G"]

def sequences_generator(file_path, length1, length2):
    new_file = open("../"+file_path, "w")

    sequence1 = ""
    for i in range(length1):
        sequence1 += possible_chars[random.randint(4)]

    sequence2 = ""
    for i in range(length2):
        sequence2 += possible_chars[random.randint(4)]

    new_file.write(sequence1+"\n")
    new_file.write(sequence1+"\n")