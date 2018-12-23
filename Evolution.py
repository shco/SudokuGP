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

