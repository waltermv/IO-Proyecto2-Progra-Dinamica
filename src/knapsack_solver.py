items_list = []
weight = 0
value = 1
identifier = 2

def knapsack_brute_force_solver(input):
    items_list[:] = input.items_list
    answer_list = []
    answer = brute_force(input.max_weight, len(items_list)-1, answer_list)
    answer_list = [[i, answer_list.count(i)] for i in set(answer_list)]
    return [answer] + answer_list

def brute_force(knapsack_weight, item_position, answer_list):
    # Caso base, capacidad negativa.
    if knapsack_weight < 0:
        return -999999

    # No queda elementos o ya nos quedamos sin capacidad en la mochila.
    if item_position < 0 or knapsack_weight == 0:
        return 0

    item = items_list[item_position]
    # Case 1. include current item n in Knapsack (v[n]) and recur for
    # remaining items (n - 1) with decreased capacity (knapsack_weight - w[n])
    include_list = answer_list+[item[identifier]]
    include = item[value] + brute_force(knapsack_weight - item[weight], item_position - 1, include_list)

    # Case 2. exclude current item n from Knapsack and recur for
    # remaining items (n - 1)
    exclude_list = answer_list
    exclude = brute_force(knapsack_weight, item_position - 1, exclude_list)

    # return maximum value we get by including or excluding current item
    if include > exclude:
        answer_list[:] = include_list
        return include
    answer_list[:] = exclude_list
    return exclude

def knapsack_dynamic_solver(input):
    items_list[:] = input.items_list
    return dynamic(input.max_weight, len(items_list)-1)

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
    answers_list = []
    while items_quantity != 0:
        if matrix[items_quantity][knapsack_weight] != matrix[items_quantity - 1][knapsack_weight]:
            if answers_list == []:
                answers_list.append([items_list[items_quantity-1][identifier], 1])
            else:
                if items_list[items_quantity-1][identifier] == answers_list[-1][0]:
                    answers_list[-1][1] += 1
                else:
                    answers_list.append([items_list[items_quantity-1][identifier], 1])
            knapsack_weight -= items_list[items_quantity-1][weight]
        items_quantity -= 1

    return [answer] + answers_list

'''items_list = [[5,20,1],[5,20,1],[5,20,1],[5,20,1],[15,50,2],[15,50,2],[15,50,2],[10,60,3],[10,60,3],[10,60,3]]
#items_list = [[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
weight = 0
value = 1
identifier = 2
answer = []

answervar = brute_force(50, len(items_list)-1, answer)
answer = [[i, answer.count(i)] for i in set(answer)]
print([answervar] + answer)
'''
#print(brute_force(50, len(items_list)-1, answer))
#print(dynamic(50, len(items_list)))