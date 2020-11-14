items_list = []
weight = 0
value = 1
identifier = 2

def knapsack_brute_force_solver(input):
    items_list = input.items_list
    answers_list = []
    answer = brute_force(input.max_weight, len(items_list), answers_list)
    return answers_list + [answer]

#fuerza bruta 2^n https://rosettacode.org/wiki/Knapsack_problem/0-1#Brute_force_algorithm
def brute_force(knapsack_weight, item_position, answers_list):
    item = items_list[item_position - 1]

    if knapsack_weight == 0 or item_position == 0:
        return 0

    if knapsack_weight < item[weight]:
        return brute_force(knapsack_weight, item_position - 1, answers_list)

    list1 = answers_list[:]
    list2 = answers_list[:]
    if list1 == []:
        list1.append([item[identifier], 1])
    else:
        if items_list[item_position-1][identifier] == list1[-1][0]:
            list1[-1][1] += 1
        else:
            list1.append([items_list[list1[-1][0]-1][identifier], 1])

    a = item[value] + brute_force(knapsack_weight-item[weight], item_position - 1, list1)
    b = brute_force(knapsack_weight, item_position - 1, list2)

    if (a > b):
        answers_list[:] = list1
        #print("resp", a, list1)
        return a
    else:
        answers_list[:] = list2
        #print("resp", a, list1)
        return b

'''
items_list = [[5,20,1],[5,20,1],[5,20,1],[5,20,1],[15,50,2],[15,50,2],[15,50,2],[10,60,3],[10,60,3],[10,60,3]]
#items_list = [[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
weight = 0
value = 1
identifier = 2

def brute_force(knapsack_weight, item_position, answers_list):
    item = items_list[item_position - 1]

    if knapsack_weight == 0 or item_position == 0:
        return 0

    if knapsack_weight < item[weight]:
        return brute_force(knapsack_weight, item_position-1, answers_list)#, answers_list

    list1 = []
    list1[:] = answers_list
    list2 = []
    list2[:] = answers_list
    if list1 == []:
        list1.append([item[identifier], 1])
    else:
        if item[identifier] == list1[-1][0]:
            list1[-1][1] += 1
        else:
            list1.append([item[identifier], 1])
    #print(list1,item_position)
    lista12 = list1[:]
    lista22 = list2[:]
    a = item[value] + brute_force(knapsack_weight-item[weight], item_position-1, lista12)
    b = brute_force(knapsack_weight, item_position-1, lista22)
    list1[:] = lista12
    list2[:] = lista22
    #print(list1,item_position)

    if (a > b):
        answers_list[:] = list1
        #print("resp", a, list1)
        return a#, list1
    else:
        answers_list[:] = list2
        #print("resp", a, list1)
        return b#, list2
       
answers_list = []
print(brute_force(50, len(items_list), answers_list))
print(answers_list)
'''

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
    answers_list = []
    while items_quantity != 0:
        if matrix[items_quantity][knapsack_weight] != matrix[items_quantity - 1][knapsack_weight]:
            if answers_list == []:
                answers_list.append([items_quantity, 1])
            else:
                if items_list[items_quantity-1][identifier] == items_list[answers_list[-1][0]][identifier]:
                    answers_list[-1][1] += 1
                else:
                    answers_list.append([items_quantity, 1])
            knapsack_weight -= items_list[items_quantity-1][weight]
        items_quantity -= 1

    return answers_list + answer
