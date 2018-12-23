class Evolution:

    def __init__(self, population, maxGenerations):
        self.population = population
        self.maxGenerations = maxGenerations

    def getBest(self):
        return self.population.getBest()

    def getWorst(self):
        return self.population.getWorst()

    def evolve(self):
        self.createReportFile()
        for gen in range(self.maxGenerations):
            self.writeGenerationData(gen)
            print("Generation" + str(gen) + ": \n" + str(self.getBest()))
            if self.getBest().isIdeal():
                break
            self.population.nextGeneration()
        if gen == self.maxGenerations:
            print("Best attempt: \n" + self.getBest())
        else:
            print("Solution: \n" + self.getBest())

        return self.getBest()

    def createReportFile(self):
        # TODO implement this method
        pass

    def writeGenerationData(self, gen):
        # TODO implement this method
        pass
