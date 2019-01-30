import timeit


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
            start = timeit.default_timer()
            self.writeGenerationData(gen)
            print("Generation" + str(gen) + ": \n" + str(self.getBest()))
            if self.getBest().isIdeal():
                break
            self.population.nextGeneration()
            stop = timeit.default_timer()
            print('Time: ', stop - start)
        if gen == self.maxGenerations:
            print("Best attempt: \n" + str(self.getBest()))
        else:
            print("Solution: \n" + str(self.getBest()))

        return self.getBest()

    def createReportFile(self):
        # TODO implement this method
        pass

    def writeGenerationData(self, gen):
        # TODO implement this method
        pass
