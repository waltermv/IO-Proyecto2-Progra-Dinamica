import random

def knapsack_generator(file_path, weight, quantity, min_weight, max_weight, min_value, max_value, min_quantity, max_quantity):
    new_file = open("../"+file_path, "w")
    new_file.write(weight+"\n")

    for i in range(quantity):
        new_weight = random.randint(min_weight, max_weight+1)
        new_value = random.randint(min_value, max_value+1)
        new_quantity = random.randint(min_quantity, max_quantity+1)
        new_file.write("{},{},{}\n".format(new_weight, new_value, new_quantity))