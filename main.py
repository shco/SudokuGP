import SudokuFileUtil as sfu
from TournamentSelection import TournamentSelection
from BoardIndividual import BoardIndividual
from Population import Population
from Evolution import Evolution

train_set = [38, 39, 40]
train_set_size = len(train_set)

pop_size = 10
max_generation = 100
max_generation = 2
mutation_prob = 0.1
crossover_prob = 0.9
good_population_percent = 0.3
height = 5
height = 3
sudoku_dim = 9

file_path = "boards//realBoards.txt"
file_util = sfu.SudokuFileUtil(file_path, sudoku_dim, train_set_size, train_set)
boards = file_util.loadPrintSudoku()

prototype = BoardIndividual(height, boards)
select = TournamentSelection(mutation_prob, crossover_prob, good_population_percent)
first_pop = Population(pop_size, prototype, select)
first_pop.replaceIndividual('(((countCellOptions+countNumPossibleAtThisCol)+(countNumPossibleAtThisBlock+countNumPossibleAtThisRow))+((countNumPossibleAtThisRow*countCellOptions)*(countCellOptions+countCellOptions)))')
evolution = Evolution(first_pop, max_generation)
best_individual = evolution.evolve()

# test
test_set = [41]
test_set_size = len(test_set)
file_util = sfu.SudokuFileUtil(file_path, sudoku_dim, test_set_size, test_set)
boards = file_util.loadPrintSudoku()

best_individual.setBoards(boards)
for i in range(len(boards)):
    best_individual.initializeGradeboard(i)
fitness = best_individual.play()
print("test_set fitness is:" + str(fitness))
