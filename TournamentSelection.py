import Selection
import random


class TournamentSelection:

    def __init__(self, mutationProb, crossoverProb, goodPopulationPercent):
        self.mutationProb = mutationProb
        self.crossoverProb = crossoverProb
        self.goodPopulationPercent = goodPopulationPercent

    def getMutationProb(self):
        return self.mutationProb

    def getCrossoverProb(self):
        return self.crossoverProb

    def getGoodPopulationPercent(self):
        return self.goodPopulationPercent

    def reproduce(self, pop, p1):
        if(random.uniform(0, 1) < self.crossoverProb):
            p2 = self.select(pop)
            p1 = p1.crossover(p2)
        if(random.uniform(0, 1) < self.mutationProb):
            p1 = p1.mutate()
        return p1

    def select(self, pop):
        return pop[randomIndex(int(len(pop) * self.goodPopulationPercent))]

    def randomIndex(self, max):
        return int(random.uniform(0, 1) * max)

