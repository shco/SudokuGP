from TerminalOrFunction import TerminalOrFunction
import copy
import math


class Terminal(TerminalOrFunction):
    
    def __init__(self, operationName):
        super().__init__("Terminal", operationName)

    def clone(self):
        return copy.deepcopy(self)

    def run(self, row, col, key, board, gradeboard):
        return Terminal.terminals.get(self.operationName)(row, col, key, board, gradeboard)

    @staticmethod
    def countEmptyCellInRow(row, col, key, board, gradeboard):
        return board[row].count(0)

    @staticmethod
    def countEmptyCellInCol(row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        return tran_board[col].count(0)

    @staticmethod
    def countEmptyCellInSquare(row, col, key, board, gradeboard):
        subSquare = Terminal.getSubSquare(row, col, board)
        return sum([row.count(0) for row in subSquare])

    @staticmethod
    def numOfOptionsInCell(row, col, key, board, gradeboard):
        return len(gradeboard[row][col])

    @staticmethod
    def numOfOptionsToAppearInBoard(row, col, key, board, gradeboard):
        return len(board) - sum([row.count(key) for row in board])

    @staticmethod
    def countEmptyCellsInRowsContainsNum(row, col, key, board, gradeboard):
        return sum([row.count(0) for row in board if key in row])

    @staticmethod
    def countEmptyCellsInColsContainsNum(row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key in row])

    @staticmethod
    def countEmptyCellsInSquareContainsNum(row, col, key, board, gradeboard):
        subSquare = Terminal.getSubSquare(row, col, board)
        return [y for x in subSquare for y in x].count(0)

    @staticmethod
    def countEmptyCellsInRows_ThatNotContainsNum(row, col, key, board, gradeboard):
        return sum([row.count(0) for row in board if key not in row])

    @staticmethod
    def countEmptyCellsInCols_ThatNotContainsNum(row, col, key, board, gradeboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key not in row])

    @staticmethod
    def countEmptyCellsInSquare_ThatNotContainsNum(row, col, key, board, gradeboard):
        flatSubSquares = [[y for x in Terminal.getSubSquare(i, j, board) for y in x] for i in range(0, len(board), int(math.sqrt(len(board)))) for j in range(0, len(board), int(math.sqrt(len(board))))]
        return sum([row.count(0) for row in flatSubSquares if key not in row])

    @staticmethod
    def getSubSquare(row, col, board):
        squareLength = int(math.sqrt(len(board)))
        if squareLength - int(squareLength):
            raise ValueError("The board is not of size NxN where N is a perfect square")
        rowRest = int(row % squareLength)
        colRest = int(col % squareLength)
        rowStartIndex = row - rowRest
        colStartIndex = col - colRest
        subSquare = [_row[rowStartIndex:rowStartIndex + squareLength] for _row in board]
        return subSquare[colStartIndex:colStartIndex + squareLength]

    @staticmethod
    def countEmptyCellInSudoku(board):
        return [y for x in board for y in x].count(0)

    terminals = {
        "countEmptyCellInRow": countEmptyCellInRow.__get__(object),
        "countEmptyCellInCol": countEmptyCellInCol.__get__(object),
        "countEmptyCellInSquare": countEmptyCellInSquare.__get__(object),
        "numOfOptionsInCell": numOfOptionsInCell.__get__(object),
        "numOfOptionsToAppearInBoard": numOfOptionsToAppearInBoard.__get__(object),
        "countEmptyCellsInRowsContainsNum": countEmptyCellsInRowsContainsNum.__get__(object),
        "countEmptyCellsInColsContainsNum": countEmptyCellsInColsContainsNum.__get__(object),
        "countEmptyCellsInSquareContainsNum": countEmptyCellsInSquareContainsNum.__get__(object),
        "countEmptyCellsInRows_ThatNotContainsNum": countEmptyCellsInRows_ThatNotContainsNum.__get__(object),
        "countEmptyCellsInCols_ThatNotContainsNum": countEmptyCellsInCols_ThatNotContainsNum.__get__(object),
        "countEmptyCellsInSquare_ThatNotContainsNum": countEmptyCellsInSquare_ThatNotContainsNum.__get__(object),
    }
