import re
import math

class SudokuFileUtil:
    def __init__(self, file_path, sudoku_dim, train_set_size, boards_to_load):
        self.file_path = file_path
        self.sudoku_dim = sudoku_dim
        self.train_set_size = train_set_size
        self.boards_to_load = boards_to_load
        self.boards = []
        self.boardsAmount = self.countBoardsInFile()
        self.checkIfValidDimensions()
        self.sudoku_num_cache = []

    def __str__(self):
        squareLength = math.sqrt(len(self.boards))
        builder = "\n"
        builder += "File path : " + str(self.file_path) + ", Boards amount : " + str(self.boardsAmount) + ", Sudoku dimension : " + str(self.sudoku_dim) +\
                  ", Sudoku num : " + str(self.sudoku_num_cache) + ", Empty cell : " + str(sum(sum(1 for i in row if i == 0) for row in self.boards))

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
        for i in range(self.train_set_size):
            if len(self.boards_to_load) < i:
                while True:
                    board_idx = random.randint(0, self.boardsAmount)
                    if board_idx not in self.sudoku_num_cache:
                        break
            else:
                board_idx = self.boards_to_load[i]
                if board_idx >= self.boardsAmount | board_idx < 0:
                    print("board num " + str(board_idx) + "is illegal")
                    continue
                if board_idx in self.sudoku_num_cache:
                    print("you choose number " + str(board_idx) + "twice")
                    continue

            self.sudoku_num_cache.append(board_idx)
            self.boards.append(self.loadSudoku(board_idx))

    def loadSudoku(self, sudoku_num):
        board = []
        founded = False
        num_of_sudoku_board_in_file = 0
        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    if founded:
                        data = re.split(r",", line)
                        place = 0
                        for i in range(self.sudoku_dim):
                            board.append([int(num) for num in data[place:place+self.sudoku_dim]])
                            place += self.sudoku_dim
                        break
                    if 'Grid' in line:
                        if sudoku_num == num_of_sudoku_board_in_file:
                            founded = True
                        else:
                            num_of_sudoku_board_in_file += 1
        except:
            print("inserted " + str(sudoku_num) + "as board index while there is only " + str(self.boardsAmount) + "boards")

        return board

    # TODO: delete this function
    def restSudoku(self, board):
        for i in range(0, self.board):
            for j in range(0, len(self.board[i])):
                self.board[i][j] = 0

    def printSudokuMain(self):
        for i in range(len(self.boards)):
            print("Sudoku :" + str(self.sudoku_num_cache[i]))
            SudokuFileUtil.printSudoku(self.boards[i])

    @staticmethod
    def printSudoku(board):
        squareLength = math.sqrt(len(board))
        zerosNum = sum(sum(1 for i in row if i == 0) for row in board)
        print("Empty cell:" + str(zerosNum))
        for i in range(len(board)):
            if i % squareLength == 0:
                print()
            toPrint = ""
            for j in range(len(board)):
                if j % squareLength == 0:
                    toPrint += "  "
                toPrint += str(board[i][j]) + " "
                if board[i][j] < 10:
                    toPrint += " "

            print(toPrint)
