class input:
    def __init__(self, file_path):
        self.read_input(file_path)

    def read_input(self, file_path):
        file = open(file_path) #"r"

        line = file.readline().split(',')
        if len(line) == 1:
            self.knapsack = True
            self.max_weight = int(line[0])

            #peso, beneficio, cantidad
            identifier = 1
            line = file.readline().split(',')
            while line != "":
                line = [int(i) for i in line]
                for i in range(line[2]):
                    self.items_list.append(line[:2].append(identifier))
                identifier += 1
                line = file.readline().split(',')
        else:
            self.knapsack = False
            self.scoring = [int(i) for i in line]

            self.row1 = file.readline()
            self.row2 = file.readline()