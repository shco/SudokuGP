import re
import math


class SudokuFileUtil:
    def __init__(self, file_path, sudoku_dim):
        self.file_path = file_path
        self.sudoku_dim = sudoku_dim
        self.boards = []
        self.boardsAmount = self.countBoardsInFile()
        self.checkIfValidDimensions()

    # def loadPrintSudoku:


    def countBoardsInFile(self):
        file_object = open(self.file_path, "r")
        word = 'grid'
        return re.split(r"[^a-z]+", file_object.read().casefold()).count(word)

    def checkIfValidDimensions(self):
        if math.sqrt(self.sudoku_dim) - int(math.sqrt(self.sudoku_dim)):
            raise ValueError('The sudoku dim is not sqrt number.')
