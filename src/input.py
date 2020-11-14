class input:
    def __init__(self, knapsack, file_path):
        if(knapsack):
            self.read_knapsack_input(file_path)
        else:
            self.read_sequences_input(file_path)

    def read_knapsack_input(self, file_path):
        file = open(file_path, "r") #"r"
        line = file.readline()

        self.max_weight = int(line)
        self.items_list = []

        #peso, beneficio, cantidad
        identifier = 1
        line = file.readline().split(',')
        while line != "":#for line in file:
            line = [int(i) for i in line]
            for i in range(line[2]):
                self.items_list.append(line[:2].append(identifier)) #Verificar
            identifier += 1
            line = file.readline().split(',')

    def read_sequences_input(self, file_path):
        file = open(file_path, "r")  # "r"

        self.sequence1 = file.readline()
        self.sequence2 = file.readline()