items_list = []
weight = 0
value = 1
identifier = 2

def knapsack_brute_force_solver(input):
    items_list = input.items_list
    answer_list = []
    answer = brute_force(input.max_weight, len(items_list), answer_list)
    return answer_list + [answer]

#fuerza bruta 2^n https://rosettacode.org/wiki/Knapsack_problem/0-1#Brute_force_algorithm
def brute_force(knapsack_weight, item_position, answer_list):
    item = items_list[item_position - 1]

    if knapsack_weight == 0 or item_position == 0:
        return 0

    if knapsack_weight < item[weight]:
        return brute_force(knapsack_weight, item_position - 1, answer_list)

    list1 = answer_list[:]
    list2 = answer_list[:]
    if list1 == []:
        list1.append([item_position, 1])
    else:
        if items_list[item_position - 1][identifier] == items_list[list1[-1][0]][identifier]:
            list1[-1][1] += 1
        else:
            list1.append([item_position, 1])

    a = item[value] + brute_force(knapsack_weight - item[weight], item_position - 1, list1)
    b = brute_force(knapsack_weight, item_position - 1, list2)

    if (a > b):
        answer_list[:] = list1
        return a
    else:
        answer_list[:] = list2
        return b

def knapsack_dynamic_solver(input):
    items_list = input.items_list
    return dynamic(input.max_weight, len(items_list))

def dynamic(knapsack_weight, items_quantity):  # sin el más en weight
    matrix = [[0 for i in range(knapsack_weight + 1)] for j in range(items_quantity + 1)]

    for item_position in range(1, items_quantity + 1):
        for actual_weight in range(knapsack_weight + 1):
            item = items_list[item_position - 1]
            if (item[weight] > actual_weight):
                matrix[item_position][actual_weight] = matrix[item_position - 1][actual_weight]
            else:
                if (item[value] + matrix[item_position - 1][actual_weight - item[weight]]) > matrix[item_position - 1][
                    actual_weight]:
                    matrix[item_position][actual_weight] = item[value] + matrix[item_position - 1][
                        actual_weight - item[weight]]
                else:
                    matrix[item_position][actual_weight] = matrix[item_position - 1][actual_weight]

    answer = matrix[items_quantity][knapsack_weight]
    answer_list = []
    while items_quantity != 0:
        if matrix[items_quantity][knapsack_weight] != matrix[items_quantity - 1][knapsack_weight]:
            if answer_list == []:
                answer_list.append([items_quantity, 1])
            else:
                if items_list[items_quantity-1][identifier] == items_list[answer_list[-1][0]][identifier]:
                    answer_list[-1][1] += 1
                else:
                    answer_list.append([items_quantity, 1])
            knapsack_weight -= items_list[items_quantity-1][weight]
        items_quantity -= 1

    return answer_list + answer
