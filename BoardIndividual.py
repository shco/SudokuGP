import Individual


class BoardIndividual(Individual):

    def __init__(self, height, board):
        super(height)
        self.originalSudoku = board
        self.board = board
        self.gradeboard = [[{} for a in range(len(board))] for b in range(len(board))]

    def isForward(self):
        dics = set([y for x in self.gradeboard for y in x])
        return len(dics) > 1 or {} not in dics
