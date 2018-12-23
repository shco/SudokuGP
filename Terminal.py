import TerminalOrFunction
import copy
import math


class Terminal(TerminalOrFunction):
    
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

    def countEmptyCellInSudoku(self, board):
        return [y for x in board for y in x].count(0)

    terminals = {
        "countEmptyCellInRow": countEmptyCellInRow,
        "countEmptyCellInCol": countEmptyCellInCol,
        "countEmptyCellInSquare": countEmptyCellInSquare,
        "numOfOptionsInCell": numOfOptionsInCell,
        "numOfOptionsToAppearInBoard": numOfOptionsToAppearInBoard,
        "countEmptyCellsInRowsContainsNum": countEmptyCellsInRowsContainsNum,
        "countEmptyCellsInColsContainsNum": countEmptyCellsInColsContainsNum,
        "countEmptyCellsInSquareContainsNum": countEmptyCellsInSquareContainsNum,
        "countEmptyCellsInRows_ThatNotContainsNum": countEmptyCellsInRows_ThatNotContainsNum,
        "countEmptyCellsInCols_ThatNotContainsNum": countEmptyCellsInCols_ThatNotContainsNum,
        "countEmptyCellsInSquare_ThatNotContainsNum": countEmptyCellsInSquare_ThatNotContainsNum,
    }
