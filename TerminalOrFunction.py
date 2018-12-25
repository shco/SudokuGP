import copy
from Node import Node


class TerminalOrFunction(Node):

    def __init__(self, nodeType, operationName):
        super(TerminalOrFunction, self).__init__()
        self.nodeType = nodeType
        self.operationName = operationName
        
    def run(self, row, col, key, board, gradeboard):
        pass

    def getNodeType(self):
        return self.nodeType

    def getOperationName(self):
        return self.operationName

    def clone(self):
        return copy.deepcopy(self)

    def isTerminal(self):
        return self.nodeType == "Terminal"

    def isFunction(self):
        return self.nodeType == "Function"

    def set(self, other):
        self.operationName = other.operationName
        self.nodeType = other.nodeType
        self.setLeft(other.getLeft())
        self.setRight(other.getRight())
