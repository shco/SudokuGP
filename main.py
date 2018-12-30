import SudokuFileUtil as sfu
from TournamentSelection import TournamentSelection
from BoardIndividual import BoardIndividual
from Population import Population
from Evolution import Evolution

boards_to_load = [38, 39, 40, 41]
train_set_size = len(boards_to_load)

pop_size = 100
max_generation = 100
mutation_prob = 0.1
crossover_prob = 0.9
good_population_percent = 0.4
height = 5
sudoku_dim = 9

file_path = "boards//realBoards.txt"
file_util = sfu.SudokuFileUtil(file_path, sudoku_dim, train_set_size, boards_to_load)
boards = file_util.loadPrintSudoku()

prototype = BoardIndividual(height, boards)
select = TournamentSelection(mutation_prob, crossover_prob, good_population_percent)
first_pop = Population(pop_size, prototype, select)

evolution = Evolution(first_pop, max_generation)
evolution.evolve()
