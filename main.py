import SudokuFileUtil as sfu
from TournamentSelection import TournamentSelection
from BoardIndividual import BoardIndividual
from Population import Population
from Evolution import Evolution
from Individual import Individual

pop_size = 10
max_generation = 100
mutation_prob = 0.1
crossover_prob = 0.9
good_population_percent = 0.4
height = 5
sudoku_dim = 9

file_path = "boards//realBoards.txt"
file_util = sfu.SudokuFileUtil(file_path, sudoku_dim)
board = file_util.loadPrintSudoku()

tree = Individual.ConvertInfixStringToTree("((((squareOfCountCellOptions*countNumPossibleAtThisRow)*(countCellOptions+countCellOptions))*((countNumPossibleAtThisRow*countNumPossibleAtThisBlock)+(countCellOptions+countNumPossibleAtThisRow)))*(((countCellOptions+countNumPossibleAtThisBlock)+(countNumPossibleAtThisBlock+countNumPossibleAtThisCol))*((countNumPossibleAtThisBlock+countCellOptions)*(countNumPossibleAtThisBlock*countNumPossibleAtThisBlock))))")
prototype = BoardIndividual(height, board)
select = TournamentSelection(mutation_prob, crossover_prob, good_population_percent)
first_pop = Population(pop_size, prototype, select)
evolution = Evolution(first_pop, max_generation)
evolution.evolve()
