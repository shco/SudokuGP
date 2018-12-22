from abc import ABC, abstractmethod
from random import choice
import copy

import operator
class Individual(ABC):
    IDEAL_FITNESS = 0
    NOT_PLAYED_YET = -1

    terminals = {
        "countEmptyCellInRow" : countEmptyCellInRow,
        "countEmptyCellInCol": countEmptyCellInCol,
        "countEmptyCellInSquare": countEmptyCellInSquare,
        "numOfOptionsInCell": numOfOptionsInCell,
        "numOfOptionsToAppearInBoard": numOfOptionsToAppearInBoard,
        "countEmptyCellsInRowsContainsNum": countEmptyCellsInRowsContainsNum,
        "countEmptyCellsInColsContainsNum": countEmptyCellsInColsContainsNum,
        "countEmptyCellsInSquareContainsNum": countEmptyCellsInSquareContainsNum,
        "countEmptyCellsInRows_ThatNotContainsNum": countEmptyCellsInRows_ThatNotContainsNum,
        "countEmptyCellsInCols_ThatNotContainsNum": countEmptyCellsInCols_ThatNotContainsNum,
        "countEmptyCellsInSquare_ThatNotContainsNum": countEmptyCellsInSquare_ThatNotContainsNum,
    }

    functions = {
        "Plus" : lambda a, b: a + b,
        "Minus" : lambda a, b: abs(a - b),
        "Multi" : lambda a, b: a * b,
        "div" : lambda a, b: a / b,
        "Mod" : lambda a, b: a % b,
        "Maximum" : lambda a, b: max(a, b),
        "Minimum" : lambda a, b: min(a, b)
    }

    @abstractmethod
    def evaluate(self):
        pass

    def __init__(self, height):
        self.fitness = NOT_PLAYED_YET
        self.height = setHeight(height)
        self.tree= generateFullTree(self.height)

    def getFitness(self):
        if self.fitness == NOT_PLAYED_YET:
            self.fitness = self.evaluate()
        return self.fitness

    def run(self, row, col, key, board, gradeboard):
        return tree.getValue().run(row, col, key, board, gradeboard)

    def setHeight(self, height):
        if height < 1:
            raise ValueError('height has to be greater or equal to 1')
        return height

    def isIdeal(self):
        return getFitness == IDEAL_FITNESS

    def getTree(self):
        return self.tree

    def cloneFullTree(self):
        return self.copyFullTree()

    def treeAsPrefixExpression(self):
        return self.ConvertTreeToPrefixExpression(self.tree)

    def treeAsInfixExpression(self):
        return self.ConvertTreeToInfixExpression(self.tree)

    def findHeight(self):
        return self.tree.findHeight()

    def generateFullTree(self, height):
        root = Node()
        createFullTree(height, root)
        return root

    def reGenerateFullTree(self):
        self.tree=generateFullTree(self.height)

    def createFullTree(self, height, node):
        if height > 0:
            node.setValue(Function(random.choice(functions.keys())))
            createSubTree(height, node)
        else:
            if height == 0:
                node.setValue(Terminal(random.choice(terminals.keys())))
                node.setLeft(None)
                node.setRight(None)
            else :
                raise ValueError('height has to be greater or equal to 1')

    def createSubTree(self, height, node):
        if height > 1:
            node.createLeft(Function(random.choice(functions.keys())))
            createSubTree(height - 1, node.getLeft())
            node.createRight(Function(random.choice(functions.keys())))
            createSubTree(height - 1, node.getRight())
        else :
            if height == 1:
                node.createLeft(Terminal(random.choice(terminals.keys())))
                node.createRight(Terminal(random.choice(terminals.keys())))
            else :
                raise ValueError('height has to be greater or equal to 1')

    def copyFullTree(self):
        cloneTree = Node(self.tree.getValue().clone())
        copySubTree(self.tree, cloneTree)
        return cloneTree

    def copySubTree(self, sourceTree, cloneTree):
        if sourceTree.getLeft() is not None:
            cloneTree.createLeft(sourceTree.getLeft().getValue().clone())
            self.copySubTree(sourceTree.getLeft(), cloneTree().getLeft())
        if sourceTree.getRight() is not None:
            cloneTree.createRight(sourceTree.getRight().getValue().clone())
            self.copySubTree(sourceTree.getRight(), cloneTree().getRight())

    def ConvertTreeToPrefixExpression(self, tree):
        st = ""
        if tree.getLeft() is not None:
            st += "( "
            st += self.ConvertTreeToPrefixExpression(tree.getLeft())
            st += " "
        if tree.getRight() is not None:
            st += self.ConvertTreeToPrefixExpression(tree.getLeft())
            st += " )"
        return st

    def ConvertTreeToInfixExpression(self, tree):
        st = ""
        if tree.getLeft() is not Node:
            st += "("
            st += self.ConvertTreeToInfixExpression(tree.getLeft())
        st  += " " + self.ConvertFromFunctionToOperator(tree.getValue().getFunctionName()) + " "
        if tree.getRight() is not None:
            st +=  self.ConvertTreeToInfixExpression(tree.getRight())
            st += ")"
        return st

    def ConvertFromFunctionToOperator(self, operationName):
        operationsName = {
            "Plus": "+",
            "Minus":"-",
            "Multi":"*",
            "div": "/",
            "Mod": "%",
            "Maximum":"Max",
            "Minimum": "Min",
        }
        return operationsName.get(operationName)

    def __str__(self):
        return "the tree as Prefix Sequence : \n" + self.treeAsPrefixExpression() + "\n\n" + self.treeAsInfixExpression()

    def clone(self):
        individual_copy = copy.deepcopy(self)
        individual_copy.setHeight(self.height)
        individual_copy.tree = self.cloneFullTree()
        individual_copy.fitness = NOT_PLAYED_YET
        return individual_copy
