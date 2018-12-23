class Population:

    def __init__(self, popSize, prototype, selection):
        self.individuals = []
        for i in range(popSize):
            self.individuals.append(prototype.clone())
            self.individuals[i].reGenerateFullTree()
        self.sort()
        self.selection = selection

    def getBest(self):
        return self.individuals[0]

    def getWorst(self):
        return self.individuals[len(self.individuals) - 1]

    def nextGeneration(self):
        newPop = []
        for i in range(len(self.individuals)):
            newPop.append(self.selection.reproduce(self.individuals, self.individuals[i]))
        self.individuals = newPop
        self.sort()

    def sort(self):
        self.individuals.sort()

    def getMutationProb(self):
        return self.selection.getMutationProb()

    def getCrossoverProb(self):
        return self.selection.getCrossoverProb()

    def getGoodPopulationPercent(self):
        return self.selection.getGoodPopulationPercent()

    def getPopulationSize(self):
        return len(self.individuals)

    def countEmptyCellInOriginalSudoku(self):
        return BoardIndividual(self.getBest()).countEmptyCellInOriginalSudoku()

    def getAvgPopulationFitness(self):
        sum = 0
        for i in range(len(self.individuals)):
            sum += self.individuals[i].getFitness()
        return sum/len(self.individuals)
    