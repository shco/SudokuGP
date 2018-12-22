import re
import math
import random

class SudokuFileUtil:
    def __init__(self, file_path, sudoku_dim):
        self.file_path = file_path
        self.sudoku_dim = sudoku_dim
        self.boards = []
        self.boardsAmount = self.countBoardsInFile()
        self.checkIfValidDimensions()
        self.sudoku_num_cache = -1

    # def loadPrintSudoku:


    def countBoardsInFile(self):
        file_object = open(self.file_path, "r")
        word = 'grid'
        return re.split(r"[^a-z]+", file_object.read().casefold()).count(word)

    def checkIfValidDimensions(self):
        if math.sqrt(self.sudoku_dim) - int(math.sqrt(self.sudoku_dim)):
            raise ValueError('The sudoku dim is not sqrt number.')

    def loadPrintSudoku(self):
        self.loadSudokuMainFunc()
        self.printSudoku()
        return self.boards

    def loadSudokuMainFunc(self):
        randomIdx = random.randint(0,self.boardsAmount)
        return self.loadSudoku(randomIdx)

    def loadSudoku(self, sudoku_num):
        if (sudoku_num >= self.boardsAmount | sudoku_num < 0):
            self.sudoku_num_cache = -1
            self.restSudoku()
            return self.boards
        if (sudoku_num == self.sudoku_num_cache):
            return self.boards

        self.sudoku_num_cache = sudoku_num
        founded = False
        numOfSudokuBoardInFile = 0
        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    print(type(f))
        except:
            print("inserted " + str(sudoku_num) + "as board index while there is only " + str(self.boardsAmount) + "boards")

    def restSudoku(self):
        for i in range(0,self.boards):
            for j in range(0,len(self.boards[i])):
                self.board[i][j] = 0


