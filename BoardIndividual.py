import Individual
import sys
import Terminal
import copy

class BoardIndividual(Individual):

    def __init__(self, height, board):
        super(height)
        self.originalSudoku = board
        self.board = board
        self.gradeboard = [[{} for a in range(len(board))] for b in range(len(board))]

    def isForward(self):
        dics = set([y for x in self.gradeboard for y in x])
        return len(dics) > 1 or {} not in dics

    def play(self):
        self.initializeGradeboard()
        fitness = self.countEmptyCellInSudoku()
        while self.isForward():
            self.evaluateGradeboard()
            min_val = sys.float_info.max
            min_row = -1
            min_col = -1
            min_key = 0
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.gradeboard[i][j] != {} and self.board[i][j] == 0:
                        for key, value in self.gradeboard[i][j].items():
                            tmp_min = value
                            if tmp_min < min_val:
                                min_key = key
                                min_row = i
                                min_col = j
                                min_val = tmp_min
            if min_row != -1 and min_col != -1 and min_key != 0:
                self.board[min_row][min_col] = min_key
                self.gradeboard[min_row][min_col] = {}
                fitness = fitness - 1
            self.initializeGradeboard()
        return fitness

    def evaluateGradeBoard(self):
        for i in range(len(self.gradeboard)):
            for j in range(len(self.gradeboard[i])):
                for key, value in self.gradeboard[i][j].items():
                    val = self.run(i, j, key, self.board, self.gradeboard)
                    self.gradeboard[i][j][key] = val

    def initializeGradeboard(self):
        for i in range(len(self.gradeboard)):
            for j in range(len(self.gradeboard[i])):
                for key, value in self.gradeboard[i][j].items():
                    self.gradeboard[i][j] = {}

    def countEmptyCellInSudoku(self):
        return Terminal.countEmptyCellInSudoku(self.board)

    def countEmptyCellInOriginalSudoku(self):
        return Terminal.countEmptyCellInSudoku(self.originalSudoku)

    def evaluate(self):
        return self.play()

    def clone(self):
        clone = copy.deepcopy(self)
        clone.board = [[val for val in row] for row in self.originalSudoku]
        clone.initializeGradeboard()

