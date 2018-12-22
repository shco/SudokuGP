import re
import math
import numpy as np
import random

class SudokuFileUtil:
    def __init__(self, file_path, sudoku_dim):
        self.file_path = file_path
        self.sudoku_dim = sudoku_dim
        self.boards = []
        self.boardsAmount = self.countBoardsInFile()
        self.checkIfValidDimensions()
        self.sudoku_num_cache = -1

    def __str__(self):
        squareLength = math.sqrt(len(self.boards))
        builder = "\n"
        builder += "File path : " + str(self.file_path) + ", Boards amount : " + str(self.boardsAmount) + ", Sudoku dimension : " + str(self.sudoku_dim) +\
                  ", Sudoku num : " + str(self.sudoku_num_cache) + ", Empty cell : " + str(sum(sum(1 for i in row if i == '0') for row in self.boards))

        builder += "\n\n"
        for i in range(len(self.boards)):
            for j in range(len(self.boards[i])):
                builder += str(self.boards[i][j]) + " "
                if (j + 1)%squareLength == 0:
                    builder += " "
            builder += "\n"
            if((i+1)%squareLength == 0):
                builder += "\n"

        return builder

    def countBoardsInFile(self):
        file_object = open(self.file_path, "r")
        word = 'grid'
        return re.split(r"[^a-z]+", file_object.read().casefold()).count(word)

    def checkIfValidDimensions(self):
        if math.sqrt(self.sudoku_dim) - int(math.sqrt(self.sudoku_dim)):
            raise ValueError('The sudoku dim is not sqrt number.')

    def loadPrintSpecificSudoku(self, sudokuNum):
        self.loadSudoku(sudokuNum)
        self.printSudokuMain()
        return self.boards

    def loadPrintSudoku(self):
        self.loadSudokuMain()
        self.printSudokuMain()
        return self.boards

    def loadSudokuMain(self):
        randomIdx = 41 #random.randint(0, self.boardsAmount)
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
                    if founded:
                        data = re.split(r",", line)
                        place = 0
                        for i in range(self.sudoku_dim):
                            self.boards.append(data[place:place+self.sudoku_dim])
                            place += self.sudoku_dim
                        break
                    if 'Grid' in line:
                        if(sudoku_num == numOfSudokuBoardInFile):
                            founded = True
                        else:
                            numOfSudokuBoardInFile += 1
        except:
            print("inserted " + str(sudoku_num) + "as board index while there is only " + str(self.boardsAmount) + "boards")

        return self.boards

    def restSudoku(self):
        for i in range(0,self.boards):
            for j in range(0, len(self.boards[i])):
                self.board[i][j] = 0

    def printSudokuMain(self):
        print("Sudoku :" + str(self.sudoku_num_cache))
        SudokuFileUtil.printSudoku(self.boards)

    @staticmethod
    def printSudoku(board):
        squareLength = math.sqrt(len(board))
        zerosNum = sum(sum(1 for i in row if i == '0') for row in board)
        print("Empty cell:" + str(zerosNum))
        for i in range(len(board)):
            if i % squareLength == 0:
                print()
            toPrint = ""
            for j in range(len(board)):
                if j % squareLength == 0:
                    toPrint += " "
                toPrint = toPrint + str(board[i][j]) + " "
            print(toPrint)
