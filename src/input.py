class input_class:
    def __init__(self, knapsack, file_path):
        self.file_path = file_path
        if(knapsack):
            self.read_knapsack_input(file_path)
        else:
            self.read_sequences_input(file_path)

    def read_knapsack_input(self, file_path):
        file = open("../"+file_path, "r") #"r"
        line = file.readline()

        self.max_weight = int(line)
        self.items_list = []

        #peso, beneficio, cantidad
        identifier = 1
        #line = file.readline()
        #line = line.rstrip('\n').split(',')
        #print(line)
        #self.weight = int(file.readline())
        #count = 0
        for line in file:
            line = list(map(int, line.split(',')))
            for i in range(line[2]):
                self.items_list.append(line[:2]+[identifier])  # Verificar
            identifier += 1

        file.close()

    def read_sequences_input(self, file_path):
        file = open("../"+file_path, "r")  # "r"

        self.sequence1 = file.readline().rstrip('\n')
        self.sequence2 = file.readline().rstrip('\n')