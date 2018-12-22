
class Selection(abc.ABC):

    @abc.abstractmethod
    def reproduce(self, pop):
        pass

    @abc.abstractmethod
    def reproduceP1(self, pop, p1):
        pass

    @abc.abstractmethod
    def getMutationProb(self):
        pass

    @abc.abstractmethod
    def getCrossoverProb(self):
        pass

    @abc.abstractmethod
    def getGoodPopulationPercent(self):
        pass
