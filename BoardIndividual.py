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

    def __str__(self):
        buf = ""
        squareLength = math.sqrt(len(self.board))
        originalEmptyCell = self.countEmptyCellInOriginalSudoku()
        currentEmptyCell = self.countEmptyCellInSudoku()
        if originalEmptyCell == currentEmptyCell:
            buf.append("this individual property not played\n\n")
        else:
            if originalEmptyCell < currentEmptyCell:
                buf.append("Solve = " + str(originalEmptyCell - currentEmptyCell) + " / " + str(originalEmptyCell) + "\nLeft" + str(currentEmptyCell) + "\n\n")
            else:
                buf.append("Something Wrong in playing function\n")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                buf.append(str(board[i][j]) + " ")
                if (j + 1) % squareLength == 0:
                    buf.append(" ")
            buf.append("\n")
            if (i+1) % squareLength == 0:
                buf.append("\n")
        buf.append(super(BoardIndividual, self).__str__(self))
        return buf

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

    def mutate(self):
        copy = self.clone()
        treeHeight = copy.tree.findHeight()
        changeInDeep = self.nextInc1ExcMax(treeHeight)
        mover = copy.tree
        parent = mover

        gen = (deep for deep in range(changeInDeep) if mover.getValue().isPrimitive())
        for deep in gen:
            parent = mover
            if random.uniform(0, 1) < 0.5:
                mover = mover.getLeft()
            else:
                mover = mover.getRight()
        self.createFullTree(treeHeight - deep, mover)
        parent.getValue().setLeft(parent.getLeft())
        parent.getValue().setRight(parent.getRight())
        return copy

    def crossover(self, object):
        copy = self.clone()
        if random.uniform(0, 1) < 0.5:
            if random.uniform(0, 1) < 0.5:
                copy.tree.setRight(copyFullTree(object.tree.getRight()))
            else:
                copy.tree.setRight(copyFullTree(object.tree.getLeft()))
        else:
            if random.uniform(0, 1) < 0.5:
                copy.tree.setLeft(copyFullTree(object.tree.getRight()))
            else:
                copy.tree.setLeft(copyFullTree(object.tree.getLeft()))
        copy.setHeight(copy.findHeight())
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
        return 1 + (random.uniform(0, 1) * (max - 1))

