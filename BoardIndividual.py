from Individual import Individual
from Terminal import Terminal
from Function import Function
import sys
import copy
import random
import math
import copy

class BoardIndividual(Individual):

    def __init__(self, height, boards):
        super(BoardIndividual, self).__init__(height)
        self.originalSudoku = copy.deepcopy(boards)
        self.boards = copy.deepcopy(boards)
        self.gradeboard = []
        self.subSquaresBoard = []
        for i in range(len(boards)):
            board = boards[i]
            self.gradeboard.append([[{} for a in range(len(board))] for b in range(len(board))])
            subSquares = [Terminal.getSubSquare(row, col, board) for row in range(0, len(board), int(math.sqrt(len(board))))
                      for col in range(0, len(board), int(math.sqrt(len(board))))]
            flatten = lambda l: [item for sublist in l for item in sublist]
            self.subSquaresBoard.append([flatten(square) for square in subSquares])

    def __str__(self):
        buf = ""
        for k in range(len(self.boards)):
            squareLength = math.sqrt(len(self.boards[k]))
            originalEmptyCell = self.countEmptyCellInOriginalSudoku(k)
            currentEmptyCell = Terminal.countEmptyCellInSudoku(self.boards[k])
            if originalEmptyCell == currentEmptyCell:
                buf += "this individual property not played\n\n"
            else:
                if currentEmptyCell < originalEmptyCell:
                    buf += "Solve = " + str(originalEmptyCell - currentEmptyCell) + " / " + str(originalEmptyCell) + "\t\t\t\t\t\t\t"
                else:
                    buf += "Something Wrong in playing function\n"
                # if currentEmptyCell < originalEmptyCell:
                #     buf += ("\nSolve = " + str(originalEmptyCell - currentEmptyCell) + " / " + str(originalEmptyCell) +
                #             "\nLeft " + str(currentEmptyCell) + "\n\n")
                # else:
                #     buf += "Something Wrong in playing function\n"
        buf += "\n"
        for k in range(len(self.boards)):
            currentEmptyCell = Terminal.countEmptyCellInSudoku(self.boards[k])
            buf += "Left " + str(currentEmptyCell) + "\t\t\t\t\t\t\t\t\t"

        buf += "\n"
        for i in range(len(self.boards[0])):
            for k in range(len(self.boards)):
                for j in range(len(self.boards[0][i])):
                    buf+=str(self.boards[k][i][j]) + " "
                    if self.boards[k][i][j] < 10:
                        buf+=" "
                    if (j + 1) % squareLength == 0:
                        buf+=" "
                buf += "\t||\t\t"
            buf+="\n"
            if (i+1) % squareLength == 0:
                buf += "\n"
        buf += super().__str__()
        return buf

    def setBoards(self, boards):
        self.originalSudoku = copy.deepcopy(boards)
        self.boards = copy.deepcopy(boards)
        self.gradeboard = []
        self.subSquaresBoard = []
        for i in range(len(boards)):
            board = boards[i]
            self.gradeboard.append([[{} for a in range(len(board))] for b in range(len(board))])
            subSquares = [Terminal.getSubSquare(row, col, board) for row in
                          range(0, len(board), int(math.sqrt(len(board))))
                          for col in range(0, len(board), int(math.sqrt(len(board))))]
            flatten = lambda l: [item for sublist in l for item in sublist]
            self.subSquaresBoard.append([flatten(square) for square in subSquares])

    def isForward(self, board_idx):
        flat_dict = [y for x in self.gradeboard[board_idx] for y in x]
        dics = [dic for dic in flat_dict if dic != {}]
        return len(dics) > 0

    def evaluateGradeboard(self, board_idx):
        gradeboard = self.gradeboard[board_idx]
        for i in range(len(gradeboard)):
            for j in range(len(gradeboard[i])):
                for key, value in gradeboard[i][j].items():
                    val = self.run(i, j, key, self.boards[board_idx], gradeboard, self.subSquaresBoard[board_idx])
                    gradeboard[i][j][key] = val

    def play(self):
        fitness = self.countEmptyCellInSudoku()
        for k in range(len(self.boards)):
            while self.isForward(k):
                self.evaluateGradeboard(k)
                min_val = sys.float_info.max
                min_row = -1
                min_col = -1
                min_key = 0
                for i in range(len(self.boards[k])):
                    for j in range(len(self.boards[k][i])):
                        if self.gradeboard[k][i][j] != {} and self.boards[k][i][j] == 0:
                            for key, value in self.gradeboard[k][i][j].items():
                                tmp_min = value
                                if tmp_min < min_val:
                                    min_key = key
                                    min_row = i
                                    min_col = j
                                    min_val = tmp_min
                if min_row != -1 and min_col != -1 and min_key != 0:
                    self.boards[k][min_row][min_col] = min_key
                    # TODO: update subsquareboard
                    self.gradeboard[k][min_row][min_col] = {}
                    fitness = fitness - 1
                self.initializeGradeboard(k)
        return fitness

    def initializeGradeboard(self, board_idx):
        board = self.boards[board_idx]
        gradeboard = self.gradeboard[board_idx]
        all_num = set(range(1, 1 + len(board)))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    row_set = set(board[i])
                    col_set = set(list(map(list, zip(*board)))[j])
                    square_set = set([y for x in Terminal.getSubSquare(i, j, board) for y in x])
                    gradeboard[i][j] = {}
                    for key in all_num - row_set - col_set - square_set:
                        gradeboard[i][j][key] = None

    def countEmptyCellInSudoku(self):
        counter = 0
        for i in range(len(self.boards)):
            counter += Terminal.countEmptyCellInSudoku(self.boards[i])
        return counter

    def countEmptyCellInOriginalSudoku(self, board_idx):
        return Terminal.countEmptyCellInSudoku(self.originalSudoku[board_idx])

    def evaluate(self):
        return self.play()

    def clone(self):
        clone = copy.deepcopy(self)
        clone.setHeight(self.height)
        clone.tree = self.cloneFullTree()
        clone.fitness = Individual.NOT_PLAYED_YET
        clone.boards = [[[val for val in row] for row in OS] for OS in self.originalSudoku]
        for i in range(len(self.boards)):
            clone.initializeGradeboard(i)
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
        copy.tree.setSize()
        copy.tree.findTreeHeight()
        object.tree.setSize()
        object.tree.findTreeHeight()
        if copy.tree.getSize() == 1 and object.tree.getSize() == 1:
            node = Function(random.choice(list(Function.functions.keys())))
            node.setRight(copy.tree)
            node.setLeft(object.tree)
            copy.tree = node
            copy.tree.setSize()
            copy.tree.findTreeHeight()
            return copy
        if copy.tree.getSize() == 1:
            copyParent = copy.tree
            copyRemoveNode = copy.tree
        else:
            copyRandNode = random.randint(2, copy.tree.getSize())
            copyParent, copyRemoveNode = copy.tree.getParentNode(copy.tree, copyRandNode)
        if object.tree.getSize() == 1:
            objectParent = object.tree
            objectRemoveNode = object.tree
        else:
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
            raise ValueError('sqrt(N) is not a natural number')
        for i in range(len(board)):
            if len(board[i]) != len(board):
                ValueError('You should send sudoku board with NxN dimensions')

    def nextInc1ExcMax(self, max):
        return random.randint(1, max)

