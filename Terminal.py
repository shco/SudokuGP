import TerminalOrFunction
import copy
import math


class Terminal(TerminalOrFunction):
    
    terminals = {
        "countEmptyCellInRow": Terminal.countEmptyCellInRow,
        "countEmptyCellInCol": Terminal.countEmptyCellInCol,
        "countEmptyCellInSquare": Terminal.countEmptyCellInSquare,
        "numOfOptionsInCell": Terminal.numOfOptionsInCell,
        "numOfOptionsToAppearInBoard": Terminal.numOfOptionsToAppearInBoard,
        "countEmptyCellsInRowsContainsNum": Terminal.countEmptyCellsInRowsContainsNum,
        "countEmptyCellsInColsContainsNum": Terminal.countEmptyCellsInColsContainsNum,
        "countEmptyCellsInSquareContainsNum": Terminal.countEmptyCellsInSquareContainsNum,
        "countEmptyCellsInRows_ThatNotContainsNum": Terminal.countEmptyCellsInRows_ThatNotContainsNum,
        "countEmptyCellsInCols_ThatNotContainsNum": Terminal.countEmptyCellsInCols_ThatNotContainsNum,
        "countEmptyCellsInSquare_ThatNotContainsNum": Terminal.countEmptyCellsInSquare_ThatNotContainsNum,
    }

    def __init__(self, operationName):
        super().__init__("Function", operationName)

    def clone(self):
        return copy.deepcopy(self)

    def run(self, row, col, key, board, gradeboard):
        Terminal.terminals.get(super().operationName)(row, col, key, board, gradeboard)

    def countEmptyCellInRow(self, row, col, key, board, gradeboard):
        board[row].count(0)

    def countEmptyCellInCol(self, row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        tran_board[col].count(0)

    def countEmptyCellInSquare(self, row, col, key, board, gradeboard):
        subSquare = self.getSubSquare(row, col, key, board, gradeboard)
        return sum([row.count(0) for row in subSquare])

    def numOfOptionsInCell(self, row, col, key, board, gradeboard):
        return len(gradeboard[row][col])

    def numOfOptionsToAppearInBoard(self, row, col, key, board, gradeboard):
        return len(board) - sum([row.count(key) for row in board])

    def countEmptyCellsInRowsContainsNum(self, row, col, key, board, gradeboard):
        return sum([row.count(0) for row in board if key in row])

    def countEmptyCellsInColsContainsNum(self, row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key in row])

    def countEmptyCellsInSquareContainsNum(self, row, col, key, board, gradeboard):
        subSquare = self.getSubSquare(row, col, key, board, gradeboard)
        return [y for x in subSquare for y in x].count(0)

    def countEmptyCellsInRows_ThatNotContainsNum(self, row, col, key, board, gradeboard):
        return sum([row.count(0) for row in board if key not in row])

    def countEmptyCellsInCols_ThatNotContainsNum(self, row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key not in row])

    def countEmptyCellsInSquare_ThatNotContainsNum(self, row, col, key, board, gradeboard):
        flatSubSquares = [[y for x in self.getSubSquare(i, j, board) for y in x] for i in range(0, len(board), int(math.sqrt(len(board)))) for j in range(0, len(board), int(math.sqrt(len(board))))]
        return sum([row.count(0) for row in flatSubSquares if key not in row])

    def getSubSquare(self, row, col, board):
        squareLength = int(math.sqrt(len(board)))
        if squareLength - int(squareLength):
            raise ValueError("The board is not of size NxN where N is a perfect square")
        rowRest = int(row % squareLength)
        colRest = int(col % squareLength)
        rowStartIndex = row - rowRest
        colStartIndex = col - colRest
        subSquare = [_row[rowStartIndex:rowStartIndex + squareLength] for _row in board]
        return subSquare[colStartIndex:colStartIndex + squareLength]
