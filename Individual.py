import random
from Node import Node
from Function import Function
from Terminal import Terminal


class Individual(object):

    IDEAL_FITNESS = 0
    NOT_PLAYED_YET = -1

    def __init__(self, height):
        self.fitness = Individual.NOT_PLAYED_YET
        self.height = self.setHeight(height)
        self.tree = None
        self.generateFullTree(self.height)
        pass

    def __eq__(self, other):
        return self.getFitness() == other.getFitness()

    def __ne__(self, other):
        return self.getFitness() != other.getFitness()

    def __lt__(self, other):
        return self.getFitness() < other.getFitness()

    def evaluate(self):
        pass

    def getFitness(self):
        if self.fitness == Individual.NOT_PLAYED_YET:
            self.fitness = self.evaluate()
        return self.fitness

    def run(self, row, col, key, board, gradeboard, squareboard):
        return self.tree.run(row, col, key, board, gradeboard, squareboard)

    def setHeight(self, height):
        if height < 1:
            raise ValueError('height has to be greater or equal to 1')
        return height

    def isIdeal(self):
        return self.getFitness() == Individual.IDEAL_FITNESS

    def getTree(self):
        return self.tree

    def cloneFullTree(self):
        return self.copyFullTree(self.tree)

    def treeAsPrefixExpression(self):
        return self.ConvertTreeToPrefixExpression(self.tree)

    def treeAsInfixExpression(self):
        return self.ConvertTreeToInfixExpression(self.tree)

    def findHeight(self):
        return self.tree.findHeight()

    def generateFullTree(self, height):
        self.tree = self.createFullTree(height)
        pass

    def reGenerateFullTree(self):
        self.generateFullTree(self.height)

    def createFullTree(self, height):
        if height > 1:
            node = Function(random.choice(list(Function.functions.keys())))
            self.createSubTree(height - 1, node)
            pass
        else:
            if height == 1:
                node = Terminal(random.choice(list(Terminal.terminals.keys())))
                node.setLeft(None)
                node.setRight(None)
            else:
                raise ValueError('height has to be greater or equal to 1')
        node.setSize()
        node.findTreeHeight()
        return node

    def createSubTree(self, height, node):
        if height > 1:
            node.setLeft(Function(random.choice(list(Function.functions.keys()))))
            self.createSubTree(height - 1, node.getLeft())
            node.setRight(Function(random.choice(list(Function.functions.keys()))))
            self.createSubTree(height - 1, node.getRight())
        else:
            if height == 1:
                node.setLeft(Terminal(random.choice(list(Terminal.terminals.keys()))))
                node.setRight(Terminal(random.choice(list(Terminal.terminals.keys()))))
            else:
                raise ValueError('height has to be greater or equal to 1')

    def copyFullTree(self, cloneTree):
        copyTree = self.tree.clone()
        self.copySubTree(self.tree, copyTree)
        return cloneTree

    def copySubTree(self, sourceTree, cloneTree):
        if sourceTree.getLeft() is not None:
            cloneTree.setLeft(sourceTree.getLeft().clone())
            self.copySubTree(sourceTree.getLeft(), cloneTree.getLeft())
        if sourceTree.getRight() is not None:
            cloneTree.setRight(sourceTree.getRight().clone())
            self.copySubTree(sourceTree.getRight(), cloneTree.getRight())

    def ConvertTreeToPrefixExpression(self, tree):
        st = " " + tree.getOperationName()
        if tree.getLeft() is not None:
            st += "( "
            st += self.ConvertTreeToPrefixExpression(tree.getLeft()) + " "
        if tree.getRight() is not None:
            st += self.ConvertTreeToPrefixExpression(tree.getRight())
            st += " )"
        return st

    def ConvertTreeToInfixExpression(self, tree):
        st = ""
        if tree is None:
            return ""
        if tree.getLeft() is not None and tree.getLeft() is not Node:
            st += "( "
            st += self.ConvertTreeToInfixExpression(tree.getLeft())
        st += " " + self.ConvertFromFunctionToOperator(tree.getOperationName()) + " "
        if tree.getRight() is not None and tree.getRight() is not None:
            st += self.ConvertTreeToInfixExpression(tree.getRight())
            st += " )"
        return st

    def ConvertFromFunctionToOperator(self, operationName):
        operationsName = {
            "Plus": "+",
            "Minus": "-",
            "Multi": "*",
            "div": "/",
            "Mod": "%",
            "Maximum": "Max",
            "Minimum": "Min",
        }
        if operationsName.get(operationName) is None:
            return operationName
        return operationsName.get(operationName)

    @staticmethod
    def ConvertInfixStringToTree(str):
        tree, _ = Individual.__ConvertInfixStringToTree__(str.replace(" ", ""))
        tree.setSize()
        tree.findHeight()
        return tree

    @staticmethod
    def __ConvertInfixStringToTree__(str):
        if str.startswith('('):
            left, str = Individual.__ConvertInfixStringToTree__(str[1:])
        isTerminal = [str.startswith(terminal) for terminal in list(Terminal.terminals.keys())]
        if any(isTerminal):
            operationName = list(Terminal.terminals.keys())[isTerminal.index(True)]
            tree = Terminal(operationName)
            return tree, str.replace(operationName, "", 1)
        isFunction = [str.startswith(terminal) for terminal in ['*', "+"]]
        if any(isFunction):
            function = Function(['*', "+"][isFunction.index(True)])
            function.setLeft(left)
            right, str = Individual.__ConvertInfixStringToTree__(str[1:])
            function.setRight(right)
            return function, str[1:]

    def __str__(self):
        return "the tree as Prefix Sequence : \n" + self.treeAsPrefixExpression() + "\n\nthe tree as Infix Sequence : \n" + self.treeAsInfixExpression()

