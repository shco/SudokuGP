from Individual import Individual
from Terminal import Terminal
import sys
import copy
import random
import math


class BoardIndividual(Individual):

    def __init__(self, height, board):
        super(BoardIndividual, self).__init__(height)
        self.originalSudoku = board
        self.board = board
        self.gradeboard = [[{} for a in range(len(board))] for b in range(len(board))]
        subSquares = [Terminal.getSubSquare(row, col, board) for row in range(0, len(board), int(math.sqrt(len(board))))
                      for col in range(0, len(board), int(math.sqrt(len(board))))]
        flatten = lambda l: [item for sublist in l for item in sublist]
        self.subSquaresBoard = [flatten(square) for square in subSquares]

    def __str__(self):
        buf = ""
        squareLength = math.sqrt(len(self.board))
        originalEmptyCell = self.countEmptyCellInOriginalSudoku()
        currentEmptyCell = self.countEmptyCellInSudoku()
        if originalEmptyCell == currentEmptyCell:
            buf += "this individual property not played\n\n"
        else:
            if currentEmptyCell < originalEmptyCell:
                buf += ("Solve = " + str(originalEmptyCell - currentEmptyCell) + " / " + str(originalEmptyCell) +
                        "\nLeft " + str(currentEmptyCell) + "\n\n")
            else:
                buf += "Something Wrong in playing function\n"
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                buf+=str(self.board[i][j]) + " "
                if self.board[i][j] < 10:
                    buf+=" "
                if (j + 1) % squareLength == 0:
                    buf+=" "
            buf+="\n"
            if (i+1) % squareLength == 0:
                buf += "\n"
        buf+=super().__str__()
        return buf

    def isForward(self):
        flat_dict = [y for x in self.gradeboard for y in x]
        dics = [dic for dic in flat_dict if dic != {}]
        return len(dics) > 0

    def evaluateGradeboard(self):
        for i in range(len(self.gradeboard)):
            for j in range(len(self.gradeboard[i])):
                for key, value in self.gradeboard[i][j].items():
                    val = self.run(i, j, key, self.board, self.gradeboard, self.subSquaresBoard)
                    self.gradeboard[i][j][key] = val

    def play(self):
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

    def initializeGradeboard(self):
        all_num = set(range(1, 1 + len(self.board)))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    row_set = set(self.board[i])
                    col_set = set(list(map(list, zip(*self.board)))[j])
                    square_set = set([y for x in Terminal.getSubSquare(i, j, self.board) for y in x])
                    self.gradeboard[i][j] = {}
                    for key in all_num - row_set - col_set - square_set:
                        self.gradeboard[i][j][key] = None

    def countEmptyCellInSudoku(self):
        return Terminal.countEmptyCellInSudoku(self.board)

    def countEmptyCellInOriginalSudoku(self):
        return Terminal.countEmptyCellInSudoku(self.originalSudoku)

    def evaluate(self):
        return self.play()

    def clone(self):
        clone = copy.deepcopy(self)
        clone.setHeight(self.height)
        clone.tree = self.cloneFullTree()
        clone.fitness = Individual.NOT_PLAYED_YET
        clone.board = [[val for val in row] for row in self.originalSudoku]
        clone.initializeGradeboard()
        return clone

    def mutate(self):
        copy = self.clone()
        randNode = random.randint(1, copy.tree.getSize())
        if randNode == 1:
            copy.tree = self.createFullTree(random.randint(1, self.height))
        else:
            parent, removeNode = copy.tree.getParentNode(copy.tree, randNode)
            if parent.left == removeNode:
                parent.setLeft(self.createFullTree(random.randint(1, parent.height)))
            if parent.right == removeNode:
                parent.setRight(self.createFullTree(random.randint(1, parent.height)))
        copy.tree.setSize()
        copy.tree.findTreeHeight()
        return copy

    def crossover(self, object):
        copy = self.clone()
        copyRandNode = random.randint(2, copy.tree.getSize())
        copyParent, copyRemoveNode = copy.tree.getParentNode(copy.tree, copyRandNode)
        objectRandNode = random.randint(2, object.tree.getSize())
        objectParent, objectRemoveNode = object.tree.getParentNode(object.tree, objectRandNode)

        if objectParent.height > copyParent.height:
            if objectParent.left == objectRemoveNode:
                objectParent.setLeft(copyRemoveNode)
            if objectParent.right == objectRemoveNode:
                objectParent.setRight(copyRemoveNode)
            object.tree.setSize()
            object.tree.findTreeHeight()
            return object
        else:
            if copyParent.left == copyRemoveNode:
                copyParent.setLeft(objectRemoveNode)
            if copyParent.right == copyRemoveNode:
                copyParent.setRight(objectRemoveNode)
            copy.tree.setSize()
            copy.tree.findTreeHeight()
            return copy

    def testIfGoodDimensionBoard(self, board):
        realSquareLength = math.sqrt(len(board))
        squareLength = int(math.sqrt(len(board)))
        if realSquareLength != squareLength:
            raise ValueError('sqrt(N) is a natural number')
        for i in range(len(board)):
            if len(board[i]) != len(board):
                ValueError('You should send sudoku board with NxN dimensions')

    def nextInc1ExcMax(self, max):
        return random.randint(1, max)

