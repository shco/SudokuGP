from TerminalOrFunction import TerminalOrFunction
import copy
import math


class Terminal(TerminalOrFunction):
    
    def __init__(self, operationName):
        super().__init__("Terminal", operationName)

    def clone(self):
        return copy.deepcopy(self)

    def run(self, row, col, key, board, gradeboard, squaresboard):
        return Terminal.terminals.get(self.operationName)(row, col, key, board, gradeboard, squaresboard)

    @staticmethod
    def methodIsTerminal(oparationName):
        return oparationName in Terminal.terminals.keys()

    @staticmethod
    def countEmptyCellInRow(row, col, key, board, gradeboard, squaresboard):
        return board[row].count(0)

    @staticmethod
    def countEmptyCellInCol(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*board)))
        return tran_board[col].count(0)

    @staticmethod
    def countEmptyCellInSquare(row, col, key, board, gradeboard, squaresboard):
        squareLength = int(math.sqrt(len(board)))
        if squareLength - int(squareLength):
            raise ValueError("The board is not of size NxN where N is a perfect square")
        rowStartIndex = row - int(row % squareLength)
        colStartIndex = col - int(col % squareLength)
        return squaresboard[rowStartIndex + int(colStartIndex / squareLength)].count(0)

    @staticmethod
    def numOfOptionsInCell(row, col, key, board, gradeboard, squaresboard):
        return len(gradeboard[row][col])

    @staticmethod
    def numOfOptionsToAppearInBoard(row, col, key, board, gradeboard, squaresboard):
        return len(board) - sum([row.count(key) for row in board])

    @staticmethod
    def countEmptyCellsInRowsContainsNum(row, col, key, board, gradeboard, squaresboard):
        return sum([row.count(0) for row in board if key in row])

    @staticmethod
    def countEmptyCellsInColsContainsNum(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key in row])

    @staticmethod
    def countEmptyCellsInSquareContainsNum(row, col, key, board, gradeboard, squaresboard):
        return sum([row.count(0) for row in squaresboard if key in row])

    @staticmethod
    def countEmptyCellsInRows_ThatNotContainsNum(row, col, key, board, gradeboard, squaresboard):
        return sum([row.count(0) for row in board if key not in row])

    @staticmethod
    def countEmptyCellsInCols_ThatNotContainsNum(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*board)))
        return sum([row.count(0) for row in tran_board if key not in row])

    @staticmethod
    def countEmptyCellsInSquare_ThatNotContainsNum(row, col, key, board, gradeboard, squaresboard):
        return sum([row.count(0) for row in squaresboard if key not in row])

    @staticmethod
    def colContainNumAndEmptyCellAtRowDiff(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*board)))
        return board[row].count(0) - sum([col.count(key) for col in tran_board if col[row] == 0]) - 1

    @staticmethod
    def rowContainNumAndEmptyCellAtColDiff(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*board)))
        return tran_board[col].count(0) - sum([row.count(key) for row in board if row[col] == 0]) - 1

    @staticmethod
    def countNumPossibleAtThisRow(row, col, key, board, gradeboard, squaresboard):
        return len([dict for dict in gradeboard[row] if key in dict]) - 1

    @staticmethod
    def countNumPossibleAtThisCol(row, col, key, board, gradeboard, squaresboard):
        tran_board = list(map(list, zip(*gradeboard)))
        return len([dict for dict in tran_board[col] if key in dict]) - 1

    @staticmethod
    def countNumPossibleAtThisBlock(row, col, key, board, gradeboard, squaresboard):
        block = Terminal.getSubSquare(row, col, gradeboard)
        return len([dict for row in block for dict in row if key in dict]) - 1

    @staticmethod
    def countCellOptions(row, col, key, board, gradeboard, squaresboard):
        return len(gradeboard[row][col].values())

    @staticmethod
    def countCellOptionsSquare(row, col, key, board, gradeboard, squaresboard):
        return (len(gradeboard[row][col].values()))**2

    @staticmethod
    def getSubSquare(row, col, board):
        squareLength = int(math.sqrt(len(board)))
        if squareLength - int(squareLength):
            raise ValueError("The board is not of size NxN where N is a perfect square")
        rowRest = int(row % squareLength)
        colRest = int(col % squareLength)
        rowStartIndex = row - rowRest
        colStartIndex = col - colRest
        subSquare = [_col[colStartIndex:colStartIndex + squareLength] for _col in board]
        return subSquare[rowStartIndex:rowStartIndex + squareLength]

    @staticmethod
    def countEmptyCellInSudoku(board):
        return [y for x in board for y in x].count(0)

    terminals = {
        # "countEmptyCellInRow": countEmptyCellInRow.__get__(object),
        # "countEmptyCellInCol": countEmptyCellInCol.__get__(object),
        # "countEmptyCellInSquare": countEmptyCellInSquare.__get__(object),
        # "numOfOptionsToAppearInBoard": numOfOptionsToAppearInBoard.__get__(object),
        # "countEmptyCellsInRowsContainsNum": countEmptyCellsInRowsContainsNum.__get__(object),
        # "countEmptyCellsInColsContainsNum": countEmptyCellsInColsContainsNum.__get__(object),
        # "countEmptyCellsInSquareContainsNum": countEmptyCellsInSquareContainsNum.__get__(object),
        # "countEmptyCellsInRows_ThatNotContainsNum": countEmptyCellsInRows_ThatNotContainsNum.__get__(object),
        # "countEmptyCellsInCols_ThatNotContainsNum": countEmptyCellsInCols_ThatNotContainsNum.__get__(object),
        # "countEmptyCellsInSquare_ThatNotContainsNum": countEmptyCellsInSquare_ThatNotContainsNum.__get__(object),
        # "colContainNumAndEmptyCellAtRowDiff": colContainNumAndEmptyCellAtRowDiff.__get__(object),
        # "rowContainNumAndEmptyCellAtColDiff": rowContainNumAndEmptyCellAtColDiff.__get__(object),
        "countNumPossibleAtThisBlock": countNumPossibleAtThisBlock.__get__(object),
        "countNumPossibleAtThisRow": countNumPossibleAtThisRow.__get__(object),
        "countNumPossibleAtThisCol": countNumPossibleAtThisCol.__get__(object),
        "countCellOptions": countCellOptions.__get__(object),
        # "squareOfCountCellOptions": countCellOptionsSquare.__get__(object),
    }
