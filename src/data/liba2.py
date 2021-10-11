class Genetic_Obj:
    def __init__(self, lenght):
        self.genome = [randint(0,1)] * lenght

    def mutate(self, rate):
        for i in range(rate):
            chose = randint(0, len(self.genome) - 1)
            if self.genome[chose] == 0:
                self.genome[chose] = 1
            else:
                self.genome[chose] = 0

    def combine(self, other):
        for i in range(len(self.genome) / 2, len(self.genome)):
            self.genome[i] = other.genome[i]

    def fitness(self, matrix):
        error = 0
        for i in range(len(matrix)):
            piv = 0
            for j in range(len(self.genome)):
                piv += self.genome[j] * matrix[i][j]
            piv = piv % 2
            if piv == 1:
                error += 1
        return error

class Genetic_SLAY:
    def __init__(self, matrix, ban):
        self.genetic_arr = [Genetic_Obj(len(matrix[0]))] * 20
        
