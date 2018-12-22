import SudokuFileUtil as sfu

pop_size = 100
max_generation = 100
mutation_prob = 0.8
crossover_prob = 0.2
good_population_percent = 0.4
height = 5
sudoku_dim = 9

file_path = "boards//realBoards.txt"
file_util = sfu.SudokuFileUtil(file_path, sudoku_dim)
board = file_util.loadPrintSudoku()

select = TournamentSelection(mutation_prob, crossover_prob, good_population_percent)
